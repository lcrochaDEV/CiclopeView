from fastapi import FastAPI
from ControlRequest.ClassRequest import Rotas
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def methodGet():
   return {"API está operacional"}


class Itens(BaseModel):
   host: str
   port: str
   device_type : str
   secret: str
   command: str

@app.get("/host")
def methodPost(itens:Itens):
      return Rotas.methodGetIdCli(itens)

@app.get("/cli")
def methodGetIdCli(itens:Itens):
      return Rotas.methodGetIdCli(itens)

@app.get("/config")
def methodGetIdConfig(itens:Itens):
      return Rotas.methodGetIdConfig(itens)
