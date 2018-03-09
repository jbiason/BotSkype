import re
import time

from skpy.msg import SkypeMsg
import bom_dia
import Calendar
import lunchTime
import mother_jokes
import fatherJokes
import pq_nasci
import blankers
import moralIncreaser
import messageContent
import misericoins_miner
import facebook_token
import bitcoin_checker

sherlocks = ["xeroque", "sherlock", "xerock", "sherock", "xeroqi", "xeroque romes"]

def handler(event):
    print(repr(event))
        
    if "#ping" in event.msg.content and event.msg.userId == "live:machado.vrs":
        msg = SkypeMsg.quote(event.msg.user, event.msg.chat, event.msg.time, event.msg.content)
        event.msg.chat.sendMsg(msg + "pong")
        
    elif event.msg.content.lower() == "bom dia silvinhobot":
        event.msg.chat.sendMsg(bom_dia.salute())

    elif "#bitcoin" in event.msg.content.lower():
        event.msg.chat.sendMsg(bitcoin_checker.formater())
        
    elif event.msg.content == "#todayLunch":
        event.msg.chat.sendMsg(lunchTime.weekday())

    elif event.msg.content == "#todayLunch(Vitor)":
        event.msg.chat.sendMsg("Massas do forte")

    elif event.msg.content == "#todayLunch(Lucas)":
        event.msg.chat.sendMsg("Abuelita")

    elif event.msg.content == "#todayLunch(Andrei)":
        event.msg.chat.sendMsg("404")

    elif event.msg.content == "#todayLunch(Gabriela)":
        event.msg.chat.sendMsg("Restaurante de luz solar")

    elif event.msg.content == "#todayLunch(Michel)":
        event.msg.chat.sendMsg("CWI Software")

    elif event.msg.content == "#todayLunch(Cleiton)":
        event.msg.chat.sendFile(open("/home/smachado/Pictures/julius.jpg", "rb"), "julius.jpg", image=True)
        
    elif event.msg.content.lower() == "#geniusss":
        event.msg.chat.sendFile(open("/home/smachado/Pictures/geniusss.jpg", "rb"), "geniusss.jpg", image=True)

    elif event.msg.content.lower() == "#genius":
        event.msg.chat.sendFile(open("/home/smachado/Pictures/Genius.jpg", "rb"), "Genius.jpg", image=True)

    elif "#mamae" in event.msg.content:
        event.msg.chat.sendMsg(mother_jokes.xingar())
        
    elif "#papai" in event.msg.content:
        event.msg.chat.sendMsg(fatherJokes.xingar())
        
    elif "por que nasci" in event.msg.content:
        event.msg.chat.sendMsg(pq_nasci.responder())
        
    elif event.msg.content.lower() in sherlocks:
        event.msg.chat.setTyping()
        event.msg.chat.sendMsg("VOCÊ DISSE...")
        time.sleep(2)
        event.msg.chat.sendMsg("Xeroque")
        time.sleep(2)
        event.msg.chat.sendMsg("Romes?")
        time.sleep(2)
        event.msg.chat.sendFile(open("/home/smachado/Pictures/xeroque.jpg", "rb"), "xeroque.jpg", image=True)
        event.msg.chat.sendMsg("Contemplem por 3s")
        time.sleep(3)

       
    elif event.msg.content == "#cardapioCantina":
        event.msg.chat.sendFile(open("/home/smachado/Pictures/cardapio_cantina.jpg", "rb"), "cardapio_cantina.jpg", image=True)

    elif event.msg.content == "#bobo" and event.msg.userId == "live:machado.vrs":
        event.msg.chat.sendFile(open("/home/smachado/Pictures/bobo.jpeg", "rb"), "bobo.jpeg", image=True)
    
    elif event.msg.content == "upupup":
        event.msg.chat.sendMsg(blankers.cleaner())

    elif 'omae wa mou shindeiru' in event.msg.content.lower():
        msg = SkypeMsg.quote(event.msg.user, event.msg.chat, event.msg.time, event.msg.content)
        event.msg.chat.setTyping()
        time.sleep(1)
        event.msg.chat.sendMsg(msg + 'NANI?')
    
    elif event.msg.content ==  "#cardapioDelicia":
        event.msg.chat.sendMsg(facebook_token.delicia())


    elif event.msg.content ==  "#cardapioAltis":
        event.msg.chat.sendMsg(facebook_token.altis())

    elif event.msg.content == "modinha":
        event.msg.chat.sendMsg('Meu pau na tua rodinha!')

        
    elif "#porra" in event.msg.content:
        event.msg.chat.setTyping()
        time.sleep(2)
        event.msg.chat.sendMsg('Porra é o cu da cachorra!')
        

    elif event.msg.content.lower() == '#viado':
        event.msg.chat.setTyping()
        time.sleep(2)
        event.msg.chat.sendMsg('Viado é rolimã, como tu e tua irmã!')


    elif event.msg.content.lower() == '#tnc':
        event.msg.chat.setTyping()
        time.sleep(2)
        event.msg.chat.sendMsg('Tomate cru é vitamina, como tu e tua prima!')
        
    elif event.msg.content == '#tnc2':
        event.msg.chat.setTyping()
        time.sleep(2)
        event.msg.chat.sendMsg('Tomate cru pra salada, e teu cu pra moçada!')
       
    elif event.msg.content.lower() == 'oloco':
        event.msg.chat.sendMsg('Meu pau no teu boco')
    
    elif event.msg.content == 'RADICAAAAL!':
        event.msg.chat.sendMsg('Teu cú no meu pau')
    elif event.msg.content == '#SilvinhoHelp':
        event.msg.chat.sendMsg('ping\npong\n#mamae\n#papai\npor que nasci\nxeroque romes\nupupup\nporra\nmodinha\n\noloco\nporra\noloco\ncachorra morreu teu cu é meu\nRADICAAAAL!\n')
    elif event.msg.content == '#tavabom':
        event.msg.chat.sendMsg('Dava pra melhor com certe..., quer dizer que ia mudar melhor... já tava bom, disse que ia mudar pra melhor, não tava muito bom, tava meio ruim também, tava ruim... agora parece que piorou! :(')
    elif ".moral()++;" in event.msg.content:
        names = ["silvio", "lucas", "vitor", "cleiton", "julio", "silvinho", "gabriela", "gaby"]
        if str(event.msg.content).lower().split('.')[0] in names:
            event.msg.chat.setTyping()
            event.msg.chat.sendMsg(moralIncreaser.moralizer(str(event.msg.content)))
        else:
            event.msg.chat.setTyping()
            event.msg.chat.sendMsg("Não dou moral pra quem não conheço!")
            # elif event.msg.content == 'pkill -9 bot':
            #     event.msg.chat.sendMsg('/me promete que vai se comportar!')
            
    # elif event.msg.content == ("#coin.help()"):
    #     event.msg.chat.sendMsg(misericoins_miner.helper())
        
    elif event.msg.content == ("#coin"):
        event.msg.chat.sendMsg(misericoins_miner.verify())
        
    elif "#coin " in event.msg.content and event.msg.userId == "live:machado.vrs":
        pattern = r'#coin (\w+) (-?[0-9]+(\.[0-9]+)?)'
        match = re.search(pattern, event.msg.content)
        if match:
            try:
                name, value = match.group(1).capitalize(), match.group(2)
                misericoins_miner.add_coins(name, float(value))
                event.msg.chat.sendMsg("Enterado :O")
            except KeyError as exc:
                event.msg.chat.sendMsg("Yo no lo conozco señor!")
        else:
            print("Num casoh")

    elif "#think" in event.msg.content:
        event.msg.chat.sendFile(open("/home/smachado/Pictures/Thinker.png", "rb"), "Thinker.png", image=True)

    elif event.msg.content == "#carinha":
        event.msg.chat.sendMsg("( ͡° ͜ʖ ͡°)")
