#!/bin/python3
import json
import requests

def replacer(word):
    replaces = ['[',']','{','}','<br/>','_','gramGrp', 'def',"'@ast", "''", ' : ',"'1'"]
    for rep in replaces:
        if rep == '<br/>':
            word = word.replace(rep, '\n')
        else:
            word = word.replace(rep, '')
    return word


def result(word):
    search = requests.get('http://dicionario-aberto.net/search-json/' + word)
    if 'superEntry' in str(search.json()):
        search = search.json()['superEntry'][0]['entry']['sense'][0]
    else:
        search = search.json()['entry']['sense'][0]['def']
    return replacer(str(search))

def elsa():
    return "Nenhum resultado encontrado"

print(result('capa'))
