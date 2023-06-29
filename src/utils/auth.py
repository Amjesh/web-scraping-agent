import os
import requests
from authlib.jose import jwt
from authlib.jose import JsonWebKey
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


# Function to verify Auth0 user token using Authlib
security = HTTPBearer()


async def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=403, detail="Invalid authentication scheme")
    try:
        token = credentials.credentials
        AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
        JWKS_URL = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'

        # Retrieve the JSON Web Key Set (JWKS) from Auth0
        jwks_response = requests.get(JWKS_URL)
        jwks = jwks_response.json()

        # Verify the JWT
        key = next(iter(jwks['keys']))
        jwk = JsonWebKey.import_key(key)
        claims = jwt.decode(token, jwk)
        print(claims)
        return claims
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=401, detail="Authentication failed!")
