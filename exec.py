#                                        ++++++++++++++++++++++++                                    
#                                  ++++++++++++          ++++++++++++++++                            
#                            ++++++++                              ++++++++++                        
#                        ++++++        ++++++++++++++++++++++++          ++++++++++                  
#                      ++++      ++++++++++++++++++++++++++++++++++++        ++++++++                
#                  ++++      ++++  ++++++++++++++++++++++++++++++  ++++++      ++++++++++            
#                ++      ++++    ++++++++++++++++++++++++++++++++++    ++++++      ++++++++          
#              ++    ++++        ++++++++++++++++++++++++++++++++++      ++++++      ++++++++++      
#          ++    ++++          ++++++++++++++          ++++++++++++          ++++++      ++++++++    
#        ++    ++              ++++++++++++            ++++++++++++++          ++++++      ++++++++  
#      ++    ++                ++        ++              ++++++++++++            ++++++      ++++++++
#    ++                        ++        ++              ++++++++++++              ++++++      ++++++
#      ++                      ++        ++              ++++++++++++              ++++++++      ++++
#                              ++++    ++++++          ++++++++++++                  ++++++++        
#                                ++++++++++++++++++++++++++++++++++                  ++++++++        
#                                ++++++++++++++++++++++++++++++++++                  ++++++++++      
#                                  ++++++++++++++++++++++++++++++                  ++++++++++++      
#                                    ++++++++++++++++++++++++++                  ++++  ++++++++      
#            ++                        ++++++++++++++++++++++                  ++++      ++++        
#                ++                        ++++++++++++++                  ++++++                    
#                    ++                                                  ++++                        
#                        ++                                          ++++                            
#                            ++++++                            ++++++                                
#                                    ++++++++++++++++++++++++                                        

#EXEMPLO COMMAND
#ClassCommand.ControllerConnect("device_type", "host", "command", 'port'(opcional, default 22), 'secret'(opcional))

from ControllerClass import ClassConsole
from ControllerClass import ClassCommand
import re


#ipEndHop = "10.18.228.193"
#ip_Destination = "10.18.228.196"
device_type = "cisco_ios_telnet"
#port = "22"
secret = ""

ipEndHop = "rack2black.hackone.com.br"
port = "41479"

#ipEndHop = input("IP End Hop: ")
#ip_Destination = input("IP Destination: ")
#port = input("Port: ")
#device_type = input("Device: ")
commandConsole = input("Command: ")


def validationText(text):
    if re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\d{2}|\w+\.\w+.com.\w+", text):
        return
    else:
        print("Host não encontrado!")  
        exit()
validationText(ipEndHop)  

#INICIO DO CONSOLE
def send_show_console_init():
    ios = ClassConsole.CommandConsole(f"{device_type}", f"{ipEndHop}", f"{commandConsole}", f"{port}")
    printInit = ios.commandInit()
    print("-"*100)
    print(f'{printInit}')
#send_show_console_init()

#INICIO DO PROGRAMA
def send_show_command_init():
    command = ["sh ver | s uptime", "sh clock", "show ip int br", "sh ver"]
    for commands in command:
        ios = ClassCommand.ControllerConnect(f"{device_type}", f"{ipEndHop}", f"{commands}", f"{port}")
        printInit = ios.commandInit()
        print("-"*100)
        print(f'{printInit}')
send_show_command_init()

#FUNÇÃO PROCURA SUB-INTERFACE

'''
command = f"show ip route {ip_Destination} | i directly connected, via"
generic = ClassCommand.ControllerConnect(f"{device_type}", f"{ipEndHop}", f"{command}", f"{port}")
endInt = generic.commandInit()
if endInt:
    sub_interface = re.findall(r"\w+?[\/\d].*", endInt)[0]
    interface = re.findall(r"\w+\w[\/\d]+|\w+\s\d+", endInt)[0]

if endInt:
    commands = [
        #"sh run | i hostname",
        #f"show ip route {ip_Destination} | i directly connected, via", 
        #f"show int {interface} | i line protocol", 
        #f"show int {interface} | i  Hardware",
        #f"show running-config interface {sub_interface} | i description",
        #"show processes | i CPU",
        #f"show arp {sub_interface}",
        #f"ping {ip_Destination}"
        #"sh ver | s uptime", #
        #"sh clock", #
        #f"show ip int br" #
        #"sh ver" #
        #f"show int {interface}" #
        ]
'''

'''
    def send_show_command(command):
        for command in commands:
            ios = ClassCommand.ControllerConnect(f"{device_type}", f"{ipEndHop}", f"{command}", f"{port}")
            #cliReturn = ios.commandExecJson()
            cliReturn = ios.commandOne()
            print("-"*100)
            print(f'{cliReturn}')

    send_show_command(commands)


def send_show_command_All():
    command = [f"show int"]
    for commands in command:
        ios = ClassCommand.ControllerConnect(f"{device_type}", f"{ipEndHop}", f"{commands}", f"{port}")
        printInit = ios.commandFilterAll()
        print("-"*100)
        #print(f'{printInit}')

        for interface in printInit:
            print(f"{interface['interface']}")
'''

#send_show_command_All()
