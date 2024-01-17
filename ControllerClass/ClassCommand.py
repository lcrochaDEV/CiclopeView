from netmiko import ConnectHandler
import json

from dotenv import load_dotenv
load_dotenv()
import os
loginDCN = os.getenv("loginDCN")
passwDCN = os.getenv("passwDCN")


class ControllerConnect:
    def __init__(self, device_type, host, command, port = "22", secret = "" ):
        self.device_type = device_type
        self.host = host
        self.command = command
        self.port = port
        self.secret = secret

    def __device__(self):
        return {
            'device_type': f'{self.device_type}',
            'host': f'{self.host}',
            'username': f'{loginDCN}',
            'password': f'{passwDCN}',
            'port' : f'{self.port}',        # optional, defaults to 22
            'secret': f'{self.secret}',     # optional, defaults to ''
        }
    
    def commandInit(self):
        try:
            connection = ConnectHandler(**self.__device__())
            return connection.send_command(f'{self.command}')       
            #print("-"*100)
            #print(f'{self.command}# \n{output}')

        except:
            print(f'Sem acesso ao Roteador {self.host}')

    def commandOne(self):
        try:
            connection = ConnectHandler(**self.__device__())
            output = connection.send_command(f'{self.command}', use_textfsm=True)
            return json.dumps(output, indent = 2)
        except:
            print(f'Sem acesso ao Roteador {self.host}')

    def commandFilterAll(self):
        try:
            connection = ConnectHandler(**self.__device__())
            return connection.send_command(f'{self.command}', use_textfsm=True)
            for interface in output:
               return f"{interface['interface']}"
        except:
            print(f'Sem acesso ao Roteador {self.host}')

    def commandConfig(self):
        with ConnectHandler(**self.__device__()) as conn:
            if not conn.check_enable_mode():
                conn.enable()
                return conn.send_config_set(self.command)
