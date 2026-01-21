from appwrite.client import Client
from appwrite.services.account import Account
from fastapi import Header, HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

def get_appwrite_client():
    client = Client()
    client.set_endpoint(os.getenv("endpoint"))
    client.set_project(os.getenv("project_id"))
    return client

def get_admin_appwrite_client():
    client = Client()
    client.set_endpoint(os.getenv("endpoint"))
    client.set_project(os.getenv("project_id"))
    client.set_key(os.getenv("api_key"))
    return client

async def get_authenticated_client(secret: str = Header(...)):
    client = get_appwrite_client()
    client.set_session(secret)
    
    try:
        account = Account(client)
        user = account.get()
        return client, user["$id"]
    except Exception:
        raise  HTTPException(status_code=401, detail="Invalid or expired session token")