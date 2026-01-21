from appwrite.services.account import Account
from auth.dependencies import get_admin_appwrite_client

client = get_admin_appwrite_client()
account = Account(client)

def register_user(email: str, password: str, name: str):
    try:
        return account.create(
            user_id="unique()",
            email=email,
            password=password,
            name=name
        )
    except Exception as e:
        return{"error": str(e)}
    
def login_user(email: str, password: str):
    try:
        session = account.create_email_password_session(
            email=email,
            password=password
        )
        return session
    except Exception as e:
        return{"error": str(e)}