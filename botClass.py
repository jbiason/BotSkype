from skpy import SkypeEventLoop, SkypeNewMessageEvent
import time
import Calendar
import mother_jokes
import fatherJokes
import pq_nasci

class SkypePing(SkypeEventLoop):
    def __init__(self, username, password):
        super(SkypePing, self).__init__(username, password)
    def onEvent(self, event):
        if not isinstance(event, SkypeNewMessageEvent):
            return
        if "ping" in event.msg.content:
            event.msg.chat.sendMsg("Pong!")
        elif "pong" in event.msg.content:
            event.msg.chat.sendMsg("Ping!")
        elif "#mamae" in event.msg.content:
            event.msg.chat.sendMsg(mother_jokes.xingar())
        elif "#papai" in event.msg.content:
            event.msg.chat.sendMsg(fatherJokes.xingar())
        elif "por que nasci" in event.msg.content:
            event.msg.chat.sendMsg(pq_nasci.responder())
        elif "xeroque romes" in event.msg.content:
            event.msg.chat.setTyping()
            event.msg.chat.sendMsg("VOCÊ DISSE...")
            time.sleep(2)
            event.msg.chat.sendMsg("Xeroque")
            time.sleep(2)
            event.msg.chat.sendMsg("Romes?")
            time.sleep(2)
            event.msg.chat.sendFile(open("/home/smachado/Pictures/xeroque.jpg", "rb"), "xeroque.jpg", image=True)
        elif "upupup" in event.msg.content:
            event.msg.chat.sendMsg('up\n'*20)
