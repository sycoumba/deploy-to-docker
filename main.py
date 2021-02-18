#from models import User
from models import User
from fastapi import FastAPI
from starlette.routing import Host
import uvicorn



app = FastAPI()

@app.post('/users/', response_model=User)

def create_user(user:User):
    return user


if __name__ == "__main__":
 uvicorn.run(app, Host = "0.0.0.0", port = 8000)