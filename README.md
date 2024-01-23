 ## Desenvolvido em Python3.11.2 <img src="./imagens/olho.png" width="50px" margin="0" padding="0">


 ### Para Instalação no Debia 12 foi criado um Ambiente Virtual
 #### Crie um ambiente virtual usando venv ou virtual env Certifique-se venv de que esteja instalado executando:
```shell
sudo apt install python3-venv
```
#### Para criar um novo ambiente virtual em um **diretório chamado env**, execute:
```shell
python3 -m venv env
```
#### Para ativar este ambiente virtual (que modifica a PATH variável de ambiente), execute:
```shell
source env/bin/activate
```
#### Agora você pode instalar uma biblioteca neste ambiente virtual:
```shell
pip install XYZ
```
Os arquivos serão instalados no env/diretório.

Se quiser sair do ambiente virtual, você pode executar:
```shell
deactivate
```
Retirado do Post [askubuntu](https://askubuntu.com/questions/1465218/pip-error-on-ubuntu-externally-managed-environment-%C3%97-this-environment-is-extern)

<font>Lembre de criair o arquivo .gitignore para evitar que essa pasta suba para o github</font>

### Instalação de Bibliotecas:

 * netmiko
 * dotenv
 * os
 * re
 * time
 * fastapi
 * uvicorn
 * pydantic

```shell
#pip install netmiko
#pip install python-dotenv
```

## Observações:
### Necessário verificar se o ntc-templates está instalado no pacote netmiko, pacote fundamentala para busca informações em formato json, caso não esteja segue o coamando.

```shell
#pip list | grep ntc-templates
```

## Comandos para Desinstalação:

```shell
#pip uninstall netmiko 
#pip uninstall --auto-remove netmiko 
#pip uninstall purge netmiko 
#pip uninstall purge netmiko 
```

### Lista de Pacotes Instalados no Windows/Linux

```shell
#netmiko          4.3.0
#ntc_templates    4.1.0
#paramiko         3.4.0
```
### Acionameto do servidor uvicorn com reload automático

```shell
#uvicorn app:app --reload
```

### Estrutura do arquivo JSON para manipulção de dados

```json
{
    "host": "192.168.0.1",
    "port": "41479",
    "device_type": "cisco_ios_telnet",
    "secret": "",
    "command": "show ver"
}
```

### Enpoints:

```
http://127.0.0.1:8000/cli
http://127.0.0.1:8000/config
```

![netmiko](https://i0.wp.com/networkautomationlane.in/wp-content/uploads/2021/08/netmiko.png?fit=640%2C244&ssl=1)



