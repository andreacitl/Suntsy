from fastapi import APIRouter, HTTPException, Depends, UploadFile, Form, File, Query
from datetime import date
from schemes.photo import Photo, UpdatePhoto
from services.photos import (
    create_photo,
    get_one_photo,
    update_photo,
    delete_photo,
    get_user_photos_by_month
)
from auth.dependencies import get_authenticated_client

router = APIRouter(prefix="/photos", tags=["Photos"])

@router.get("/by-month")
async def get_photos(
    year: int = Query(..., example=2026),
    month: int = Query(..., ge=1, le=12),
    auth=Depends(get_authenticated_client)
):
    client, user_id = auth

    return get_user_photos_by_month(
        client=client,
        user_id=user_id,
        year=year,
        month=month
    )

@router.get("/{doc_id}")
async def get_photo_endpoint(
    doc_id: str,
    auth=Depends(get_authenticated_client)
    ):
    client, id = auth
    photo_doc = get_one_photo(client=client, doc_id=doc_id)
    return photo_doc

@router.post("/")
async def new_photo(
    caption: str = Form(None),
    location: str = Form(None),
    day: date = Form(...),  
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

@router.put("/{doc_id}")
async def update_photo_endpoint(
    doc_id: str,
    caption: str = Form(None),
    location: str = Form(None),
    day: date = Form(None), 
    file: UploadFile = File(None),
    auth=Depends(get_authenticated_client)
):
    client, id = auth
    ALLOWED_TYPES = ["image/jpeg", "image/png"]

    if file and file.filename:
        if file.content_type not in ALLOWED_TYPES:
            raise HTTPException(
                status_code=400,
                detail="Tipo de archivo no permitido"
            )


    update_photo_data = UpdatePhoto(
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
