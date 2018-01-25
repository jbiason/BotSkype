from botClass import SkypePing
sk = SkypePing('silvinho485@gmail.com', '$Ilvio141091') # connect to Skype

sk.user # you
sk.contacts # your contacts
sk.chats # your conversations

# ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
ch = sk.contacts["live:machado.vrs"].chat # 1-to-1 conversation

ch.sendMsg("ACORDEI!") # plain-text message
# ch.sendFile(open("song.mp3", "rb"), "song.mp3") # file upload
# ch.sendContact(sk.contacts["daisy.5"]) # contact sharing
ch.getMsgs() # retrieve recent messages
sk.loop()
