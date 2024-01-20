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
 * json
 * os
 * re
 * time



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

### Lista de Pacotes Instalados no Windows/Linux

```shell
#netmiko          4.3.0
#ntc_templates    4.1.0
#paramiko         3.4.0
```


![netmiko](https://i0.wp.com/networkautomationlane.in/wp-content/uploads/2021/08/netmiko.png?fit=640%2C244&ssl=1)



