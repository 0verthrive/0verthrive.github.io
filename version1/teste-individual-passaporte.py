import json
import re
import requests


def getPassport(IdentifyCode):
    # Criando discionário para a api
    prt = requests.get('https://0verthrive.github.io/prt.json')
    dict_prt = prt.json()['prt']

    # Definindo padrão para comparar
    identity = r"^(\w{3,3})\s?(\d{9,9})$"

    # Comparando o padrão com a entrada do usuário
    match = re.search(identity, IdentifyCode)

    # Percorrendo o dicionário
    if match.group(1) == 'prt':
        for item in dict_prt:
            for value in item.values():
                if str(match.group(2)) == str(value):
                    return True


var = getPassport(input())

if var:
    print("Entrou")
else:
    print("num rolou")