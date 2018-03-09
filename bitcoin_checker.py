#!/bin/python3
import json
import requests
from datetime import datetime

def _format_time(date):
    now = datetime.fromtimestamp(date['ticker']['date'])    
    dia, mes, ano, hora, minuto = now.day,  now.month, now.year, now.hour, now.minute
    return "Consultado em - {}/{}/{} - {}:{}".format(dia, mes, ano, hora, minuto)

def _last_value(req):
    last_val = req['ticker']['last']
    return 'Ultimo valor - {}'.format(last_val)

def _higher_value(req):
    higher_val = req['ticker']['high']
    return 'Maior - {}'.format(higher_val)

def _lower_value(req):
    lower_val = req['ticker']['low']
    return 'Menor - {}'.format(lower_val)

def _total_volume(req):
    total_vol = req['ticker']['vol']
    return 'Volume do dia - {}'.format(total_vol)

def formater():
    
    req = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/').json()
    return "\tMercado Bitcoin - BRL/BTC\n{}\n{}\n{}\n{}\n{}".format(
        _last_value(req),
        _higher_value(req),
        _lower_value(req),
        _total_volume(req),
        _format_time(req)
    )


