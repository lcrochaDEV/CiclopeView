from connect_netmiko.execComand import *
import re

class Rotas:
    @staticmethod
    def methodGetIdCli(itens):
      if re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\w+.com.\w+", itens.host):
            return send_show_commandExe(itens)
      else:
            return 'Host não encontrado!'
      
    @staticmethod
    def methodGetIdConfig(itens):
      if re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\w+.com.\w+", itens.host):
            return send_show_commandConfig(itens)
      else:
            return 'Host não encontrado!'
