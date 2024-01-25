from fastapi import FastAPI
from ControlRequest.ClassRequest import Rotas
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/host")
def methodPost(itens:Itens):
      return Rotas.methodGetIdCli(itens)

@app.get("/cli")
def methodGetIdCli(itens:Itens):
      return Rotas.methodGetIdCli(itens)

@app.get("/config")
def methodGetIdConfig(itens:Itens):
      return Rotas.methodGetIdConfig(itens)
