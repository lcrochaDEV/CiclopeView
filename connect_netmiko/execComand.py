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

from connect_netmiko.ControllerClass.ClassCommand import ControllerConnect
# FUNÇÃO GET
def send_show_command_init(itens: list):
    command = ["show ip int br"]
    for commands in command:
        ios = ControllerConnect(f"{itens.username}", f"{itens.password}", f"{itens.device_type}", f"{itens.host}", f"{commands}", f"{itens.port}")
        return ios.commandExe()

def send_show_commandExe(itens: list):
    ios = ControllerConnect(f"{itens.username}", f"{itens.password}", f"{itens.device_type}", f"{itens.host}", f"{itens.command}", f"{itens.port}")
    return ios.commandExe()

def send_show_commandConfig(itens: list):
    command = eval(itens.command)
    ios = ControllerConnect(f"{itens.username}", f"{itens.password}", f"{itens.device_type}", f"{itens.host}", command, f"{itens.port}")
    return ios.commandConfig()
