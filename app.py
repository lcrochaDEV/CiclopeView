from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ControlRequest.ClassRequest import Rotas
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)

@app.get("/")
def methodGet():
   return {"API está operacional"}

class Itens(BaseModel):
   username: str
   password: str
   device_type : str
   command: str
   host: str
   port: str
   secret: str

@app.post("/host")
def methodPost(itens:Itens):
      return Rotas.methodPostIdCli(itens)

@app.post("/cli")
def methodPostIdCli(itens:Itens):
      return Rotas.methodPostIdCli(itens)

@app.post("/config")
def methodPostIdConfig(itens:Itens):
      return Rotas.methodPostIdConfig(itens)
