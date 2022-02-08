from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

service_account_tokens = {
    "some_service" : 'your_random_auth_key'
}

def validate_token(token: str = Depends(oauth2_scheme)):
    if service_account_tokens['some_service'] != token:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return "authenticated"
