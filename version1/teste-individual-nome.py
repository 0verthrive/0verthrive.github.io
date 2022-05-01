import fuzzywuzzy as fuzzy
from fuzzywuzzy import process
import json
import requests

def getMatch(field):
  lista = requests.get('https://cspinheiro.github.io/interpol.json')
  search_list = process.extract(field, lista)
  result = []

  for name in search_list:
    if name[1] > 80:
      result.append(name)
  if len(result) == 0:
    return 'Pode entrar no país'
  else:
    return 'Não pode entrar no país'

getMatch(input())