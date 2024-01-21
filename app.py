from fastapi import FastAPI
import re
import execComand
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
async def methodPost(itens:Itens):
   if re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\d{2}|\w+\.\w+.com.\w+", itens.host):
      return execComand.send_show_command_init(itens)   
   else:
      print("Host não encontrado!")  
      exit()

@app.get("/cli")
def methodGetId(itens:Itens):
   if re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\d{2}|\w+\.\w+.com.\w+", itens.host):
      return execComand.send_show_commandExe(itens)
   else:
      print("Host não encontrado!")  
      exit()

@app.get("/config")
def methodGetId(itens:Itens):
   if re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\d{2}|\w+\.\w+.com.\w+", itens.host):
      return execComand.send_show_commandConfig(itens)
   else:
      print("Host não encontrado!")  
      exit()