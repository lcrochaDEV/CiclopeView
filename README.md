## Desenvolvido em Python3.11.2

### Instalação de Bibliotecas:

 * Biblioteca [netmiko](https://pypi.org/project/netmiko/), apenas na versão 2.4.2 e não está integrado o pacote [ntc-templates](https://pypi.org/project/ntc-templates/4.0.1/) nas versão do Debian, na versão Windows o pacote é mais completo, e vem com o ntc-templates default.

```shell
#sudo apt install python3-netmiko
#sudo apt install python3-dotenv
```

## Observações:
### Necessário verificar se o ntc-templates está instalado no pacote.

```shell
#pip list | grep ntc-templates
```

## Comandos para Desinstalação:

```shell
#sudo apt-get remove python3-netmiko 
#sudo apt-get remove --auto-remove python3-netmiko 
#sudo apt-get purge python3-netmiko 
#sudo apt-get purge python3-netmiko 
```

### Lista de Pacotes Instalados no Windows

```shell
#netmiko          4.3.0
#ntc_templates    4.1.0
#paramiko         3.4.0
```

![netmiko](https://i0.wp.com/networkautomationlane.in/wp-content/uploads/2021/08/netmiko.png?fit=640%2C244&ssl=1)


