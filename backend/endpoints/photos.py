from fastapi import APIRouter, Body, HTTPException, Depends, UploadFile, Form, File
from schemes.photo import Photo, UpdatePhoto
from services.photos import create_photo, get_one_photo, update_photo, delete_photo, get_all_user_photos
from auth.dependencies import get_authenticated_client
from datetime import datetime

router = APIRouter()

@router.get("/photos/{doc_id}")
async def get_photo_endpoint(
    doc_id: str,
    auth=Depends(get_authenticated_client)
    ):
    client, id = auth
    photo_doc = get_one_photo(client=client, doc_id=doc_id)
    return photo_doc

@router.post("/photos")
async def new_photo(
    caption: str = Form(None),
    location: str = Form(None),
    day: str = Form(...),
    file: UploadFile = File(...),
    auth=Depends(get_authenticated_client)
):
    client, id = auth
    ALLOWED_TYPES = ["image/jpeg", "image/png"]

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido")
    
    photo_data = Photo(
        caption=caption,
        location=location,
        day=day,
        user_id=id
    )
    return create_photo(photo_data, client, id, file)

@router.put("/photos/{doc_id}")
async def update_photo_endpoint(
    doc_id: str,
    caption: str = Form(None),
    location: str = Form(None),
    day: str = Form(...),
    file: UploadFile = File(None),
    auth=Depends(get_authenticated_client)
):
    client, id = auth
    ALLOWED_TYPES = ["image/jpeg", "image/png"]

    if file is not None and file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido")

    update_photo_data = Photo(
        caption=caption,
        location=location,
        day=day,
        user_id=id,
    )
    return update_photo(doc_id, update_photo_data, client, id, file)

@router.delete("/{doc_id}")
def delete_photo_endpoint(
    doc_id: str,
    auth=Depends(get_authenticated_client)
    ):
    client, id = auth
    # La llamada a la función de servicio debe incluir el cliente de Appwrite
    response = delete_photo(client=client, doc_id=doc_id)
    return response
  
@router.get("/all")
def get_all_photos_endpoint(
    auth=Depends(get_authenticated_client)
    ):
    client, user_id = auth
    photos_list = get_all_user_photos(client=client, user_id=user_id)
    return photos_list