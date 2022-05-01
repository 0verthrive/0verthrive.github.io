from pyngrok import ngrok
from fuzzywuzzy import process
import json
import streamlit as st
import re
import requests


def getName(name):
    listInterpol = requests.get('https://cspinheiro.github.io/interpol.json')
    search_list = process.extract(name, listInterpol)
    result = []
    for name in search_list:
        if name[1] > 80:
            result.append(name)
    if len(result) != 0:
        return True


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


def main():
    html_temp = """
    <body style="background-color:black">
    <div style ="background-color:#0000FF;padding:13px"> 
    <h1 style ="color:white;text-align:center;">UE-SIS</h1> 
    </div>
    <br/>
    </body> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    passengerName = st.text_input('Full name:')
    identifyPass = st.text_input('Identification code:')
    if st.button("Verificar"):
        if (getName(passengerName)) or (getPassport(identifyPass)):
            return st.warning("Não pode entrar no país")
        else:
            return st.success("Pode entrar no país")


if __name__ == '__main__':
    main()