from ControllerClass import ClassCommand
import re

#EXEMPLO COMMAND
#ClassCommand.ControllerConnect("device_type", "host", "command", 'port'(opcional, default 22), 'secret'(opcional))

#ipEndHop = "10.18.228.193"
ipEndHop = "rack2black.hackone.com.br"
#ip_Destination = "10.18.228.196"
device_type = "cisco_ios_telnet"
port = "41479"

#ipEndHop = input("IP End Hop: ")
#ip_Destination = input("IP Destination: ")
#port = input("Port: ")
#device_type = input("Device: ")

#ipEndHop = input("IP End Hop: ")

'''
def validationText(text):
    if re.findall(r"\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}|\w+\.\w+", text)[0]:
        #send_show_command_init()
    else:
        print("Host não encontrado!")  
        exit()

validationText(ipEndHop)
'''
#\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}|\w+\s\w+\.\w+

#INICIO DO PROGRAMA
def send_show_command_init():
    command = ["sh ver | s uptime", "sh clock", f"show ip int br", "sh ver"]
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
