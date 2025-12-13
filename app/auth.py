from jose import jwt, JWTError

SECRET_KEY = "django-insecure-wi6(etcqol1rtepnnil59jonus31oyu-v3c$l$h(#&3%*hdeu5"
ALGORITHM = "HS256"

from fastapi import Request, HTTPException, Depends

def verify_jwt(request: Request):
    # Cookie-dan token olish
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token not found")


    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
