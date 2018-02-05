#!/bin/python3
import json
file_path = "/home/smachado/Documents/Gambiarras/skypeBot/usuarios.json"
users = {"Silvio":0.0,
         "Vitor":0.0,
         "Cleiton":0.0,
         "Lucas":0.0,
}


def save():
    with open(file_path, "w") as usuarios:
        json.dump(users, usuarios)

def load():
    global users
    try:
        with open(file_path, "r") as usuarios:
            users = json.load(usuarios)
    except FileNotFoundError as exc:
        pass

def add_coins(user, value):
    users[user] += value
    save()

def verify():
    output = ""
    format_string = "    {:12}|     {:<12}\n"
    output += format_string.format("Name", "Wallet")

    for user, value in users.items():
        output += format_string.format(user, value)
    return "{code}"+output+"{code}"
load()

def helper():
    return """{code}       Mineirador de misericoins

comandos:
#coin - Mostra o ranking geral
#coin usuario valor - Adiciona o valor para o usuario.
Exemplo - '#coin Lucas 0.1'
Misericoins podem ser subtraidas adicionando '-' antes/junto ao valor (-0.5)
Obs: Só pode ser passado um valor e um usuario por vez.
O bot só escuta a Gabriela, como ela é nosso gerador de miseiricoins, a mesma não possui placar.
Usuarios: Cleiton, Silvio, Vitor, Lucas, Julio. # Exatamente como escrito aqui
{code}"""
