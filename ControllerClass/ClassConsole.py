
from ControllerClass import ClassCommand
from netmiko import ConnectHandler
import json

class CommandConsole(ClassCommand.ControllerConnect):
    def __init__(self, device_type, host, command, port = "22", secret = "" ):
        super().__init__(device_type, host, command, port, secret = "" )

'''
    def commandConfig(self):
        with ConnectHandler(**self.__device__()) as conn:
            if not conn.check_enable_mode():
                conn.enable()
                return conn.send_config_set(self.command)
'''

