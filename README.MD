# IoT Project » Bluetooth BLE

Desenvolvimentos de uma solução de IoT para a monitorização das atividades de uma pulseira Mi Band 3.
- Monitorizar número de passos.
- Monitorizar a bateria.
- Monitorizar batimentos cardíacos.
- Estabelecimento de mecanismos de poupança de bateria.


## Tasks

- Ler as Mi Band 3 presentes, através do Scanner.
- Aceder aos determinados servidos na pulseira:
    - Número de passos.
    - Nível da bateria.
    - Batimento cardíaco.
- MOM
- Impementar um servidor de GATT (o que vai ler a pulseira: gatway) completo (os sensores de serviços diferentes devem ser implementados como características independentes de serviços independentes)

## Install dependencies
```
pip install -r requirements.txt
```
## Description dependency libraries

- bluepy 1.3.0  
pip install bluepy  
https://pypi.org/project/bluepy/

- pip install pycryptodomex (Use: from Cryptodome.Cipher import AES)

## How to run the project

```
sudo python3 scanner.py
```

## Possible my Mi Band 3
```
Device ce:66:3c:61:74:19 (random), RSSI=-53 dB
 Flags = 06
 Manufacturer = 5701006130ba7b79e7b87970a2af426955b75d01ce663c617419
 Complete Local Name = Mi Band 3
 Incomplete 16b Services = 0000fee0-0000-1000-8000-00805f9b34fb
 ```

## Tarefas a fazer
- Thread que faça o Scanner (transpor o código do Scan para dentro de uma Thread)
- É possivel le-la? Então lê e realiza utiliza uma MOM para manipular os dados
    MOM: message oriented mid

## Próxima aula
- Mecanismos de envio de mensagens

## Utilizades

- restart Bluetooth from terminal
```
sudo systemctl restart bluetooth
```

## Anotações

Minha Mi Band 3: 'ce:66:3c:61:74:19'

O code para scanner da pulseira está na página 6 do ficheiro "Apresent8 - BLE Dev.pdf"
Working with notifications (página 7) é para o pessoal que vai usar Arduino

Ler dados de um ficheiro:  
```python
file_name = 'miband-mac-address.txt'
    file_miband = open(file_name, 'r')
    mibands_from_file = file_miband.readlines()

    if not len(mibands_from_file):
        print('You don\'t have any Mi Band 3 setted in {}.'.format(file_name))
```