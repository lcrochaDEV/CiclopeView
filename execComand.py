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

from ControllerClass import ClassCommand
import json
# FUNÇÃO GET

def send_show_command_init(itens):
    command = ["show ip int br"]
    for commands in command:
        ios = ClassCommand.ControllerConnect(f"{itens.device_type}", f"{itens.host}", f"{commands}", f"{itens.port}")
        return ios.commandExe()

def send_show_commandExe(itens):
    ios = ClassCommand.ControllerConnect(f"{itens.device_type}", f"{itens.host}", f"{itens.command}", f"{itens.port}")
    return ios.commandExe()

def send_show_commandConfig(itens):
    command = eval(itens.command)
    ios = ClassCommand.ControllerConnect(f"{itens.device_type}", f"{itens.host}", command, f"{itens.port}")
    return ios.commandConfig()
