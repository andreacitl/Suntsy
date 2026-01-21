from fastapi import APIRouter, Body, HTTPException
from schemes.users import UserLogin, UserRegister
from services.user import register_user, login_user
router = APIRouter()


@router.post("/sign-up")
def register(user: UserRegister):
    result = register_user(user.email, user.password, user.name)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return {"msg": "User registered", "user": result}

@router.post("/log-in")
def loing(user: UserLogin):
    result = login_user(user.email, user.password)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return {"msg": "Login sucessful", "session": result}