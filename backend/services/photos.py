
from fastapi import UploadFile, HTTPException
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from appwrite.services.account import Account
from appwrite.client import Client
from appwrite.query import Query 
from appwrite.input_file import InputFile
from schemes.photo import Photo
from datetime import date
import tempfile
from auth.dependencies import get_appwrite_client
import os

def get_user_photos_by_month(
    client,
    user_id: str,
    year: int,
    month: int
):
    # Calcular rango de fechas
    start_date = date(year, month, 1)

    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)

    databases = Databases(client)
    collection_id = os.getenv("collect_id")
    database_id = os.getenv("db_id")

    queries = [
        Query.equal("user_id", user_id),
        Query.greater_than_equal("day", start_date.isoformat()),
        Query.less_than("day", end_date.isoformat())
    ]

    try:
        response = databases.list_documents(
            database_id=database_id,
            collection_id=collection_id,
            queries=queries
        )

        return response["documents"]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al listar fotos del usuario '{user_id}' para {year}-{month}: {str(e)}"
        )

def get_one_photo(client, doc_id: str):
    databases = Databases(client)
    collection_id = os.getenv("collect_id")
    database_id = os.getenv("db_id")
    
    try:
        doc = databases.get_document(
            database_id=database_id,
            collection_id=collection_id,
            document_id=doc_id
        )
        return doc
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Documento con ID '{doc_id}' no encontrado o error de Appwrite: {str(e)}")

def create_photo(photo: Photo, client, user_id: str, file: UploadFile):
    databases = Databases(client)
    storage = Storage(client)

    collection_id = os.getenv("collect_id")
    database_id = os.getenv("db_id")
    bucket_id = os.getenv("bucket")

    tmp_path = None
    image_id = None

    try:
        file_extension = file.filename.split('.')[-1] if '.' in file.filename else 'tmp'
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp:
            file.file.seek(0) 
            tmp.write(file.file.read())
            tmp_path = tmp.name
            
        uploaded = storage.create_file(
            bucket_id=bucket_id,
            file_id="unique()",
            file=InputFile.from_path(tmp_path) 
        )
        image_id = uploaded["$id"]

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al subir imagen: {str(e)}")
    
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)

    if not image_id:
        raise HTTPException(status_code=500, detail="Fallo interno: No se obtuvo ID de imagen de Appwrite.")

    try:
        doc = databases.create_document(
            database_id=database_id,
            collection_id=collection_id,
            document_id="unique()",
            data={
                "caption": photo.caption,
                "location": photo.location,
                "user_id": user_id,
                "imagen_id": image_id,
                "day": photo.day.isoformat() if photo.day else None
            }
        )
        return doc
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear documento: {str(e)}")


def update_photo(doc_id: str, photo: Photo, client, user_id: str, file: UploadFile = None):
    databases = Databases(client)
    storage = Storage(client)

    collection_id = os.getenv("collect_id")
    database_id = os.getenv("db_id")
    bucket_id = os.getenv("bucket")
    
    photo_data_dict = photo.model_dump()
    
    update_data = {
        key: value for key, value in photo_data_dict.items() 
        if value is not None and key != 'user_id'
    }
        # Convertir day a string si viene en el update
    if "day" in update_data and isinstance(update_data["day"], date):
        update_data["day"] = update_data["day"].isoformat()

    
    image_id = None
    tmp_path = None
    old_image_id = None
    
    try:
        old_doc = databases.get_document(
            database_id=database_id,
            collection_id=collection_id,
            document_id=doc_id
        )
        old_image_id = old_doc.get("imagen_id")
    except Exception:
        pass

    if file and file.filename:
        try:
            file_extension = file.filename.split('.')[-1] if '.' in file.filename else 'tmp'
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp:
                file.file.seek(0) 
                tmp.write(file.file.read())
                tmp_path = tmp.name
                
            uploaded = storage.create_file(
                bucket_id=bucket_id,
                file_id="unique()",
                file=InputFile.from_path(tmp_path) 
            )
            image_id = uploaded["$id"]
            
            if old_image_id:
                try:
                    storage.delete_file(bucket_id=bucket_id, file_id=old_image_id)
                except Exception as e:
                    print(f"Advertencia: No se pudo borrar el archivo anterior {old_image_id}: {e}")

        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error al subir nueva imagen: {str(e)}")
        
        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
            
        update_data["imagen_id"] = image_id

    if not update_data:
         return databases.get_document(database_id=database_id, collection_id=collection_id, document_id=doc_id)
         
    try:
        doc = databases.update_document(
            database_id=database_id,
            collection_id=collection_id,
            document_id=doc_id, 
            data=update_data
        )
        return doc
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al actualizar el documento {doc_id} o permisos insuficientes: {str(e)}")


def delete_photo(client: Client, doc_id: str):
    databases = Databases(client)
    storage = Storage(client)
    collection_id = os.getenv("collect_id")
    database_id = os.getenv("db_id")
    bucket_id = os.getenv("bucket")
    
    try:
        old_doc = databases.get_document(
            database_id=database_id,
            collection_id=collection_id,
            document_id=doc_id
        )
        old_image_id = old_doc.get("imagen_id")
        storage.delete_file(bucket_id=bucket_id, file_id=old_image_id)
        
        databases.delete_document(
            database_id=database_id,
            collection_id=collection_id,
            document_id=doc_id,             
        )
        return {"status": "success", "detail": f"Documento {doc_id} eliminado"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

