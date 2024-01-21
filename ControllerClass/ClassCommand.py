from netmiko import ConnectHandler
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
    
    def commandExe(self):
        try:
            connection = ConnectHandler(**self.__device__())
            return connection.send_command(f'{self.command}', use_textfsm=True)
        except:
            print(f'Sem acesso ao Roteador {self.host}, consulte o Administrador')

    def commandConfig(self):
        try:
            with ConnectHandler(**self.__device__()) as conn:
                if not conn.check_enable_mode():
                    conn.enable()
                    conn.send_config_set(self.command)
                    return 'Comandos Realizado com sucesso!'
        except:
            print(f'Sem acesso ao Roteador {self.host}, consulte o Administrador')

