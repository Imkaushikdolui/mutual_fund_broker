from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from dotenv import dotenv_values
import jwt
from jwt.exceptions import PyJWTError
from datetime import datetime, timedelta
import uvicorn
import requests

app = FastAPI()

# Load environment variables from .env file
env_values = dotenv_values(".env")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Secret key for JWT token
SECRET_KEY = env_values.get("SECRET_KEY")
ALGORITHM = env_values.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(env_values.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Dummy credentials
dummy_username = env_values.get("USERNAME")
dummy_password = env_values.get("PASSWORD")

# Rapid api keys
x_rapidapi_key = env_values.get("X_RAIDAPI_KEY")
x_rapidapi_host = env_values.get("X_RAIDAPI_HOST")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    print("Received username:", username)
    print("Received password:", password)

    print("Stored username:", dummy_username)
    print("Stored password:", dummy_password)

    if username != dummy_username or password != dummy_password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Generate JWT token
    access_token = create_access_token(username)
    print("Generated token:", access_token)

    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie("access_token", access_token.decode(), httponly=True)  # Convert token to string
    return response

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    token = request.cookies.get("access_token")
    print("Received token:", token, type(token))
    if not token:
        return RedirectResponse(url="/", status_code=303)

    # Validate token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except PyJWTError as e:
        print("Error decoding token:", e)
        raise HTTPException(status_code=401, detail="Invalid token")

    return templates.TemplateResponse("dashboard.html", {"username": username, "request": request})

@app.get("/scheme/{scheme_code}")
async def get_scheme_details(request: Request, scheme_code: str):
    # Check if scheme code exists
    if scheme_code:

        url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"

        querystring = {"Scheme_Code":scheme_code}

        headers = {
        	"X-RapidAPI-Key": x_rapidapi_key,
        	"X-RapidAPI-Host": x_rapidapi_host
        }

        response = requests.get(url, headers=headers, params=querystring)

        scheme = response.json()
        return templates.TemplateResponse("scheme_details.html",{"request": request,"scheme": scheme})
    else:
        raise HTTPException(status_code=404, detail="Scheme not found")

def create_access_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": username, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
