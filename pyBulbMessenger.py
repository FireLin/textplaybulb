import telegram
from telegram.ext import Updater, MessageHandler, Filters
from requests import put


url = 'http://127.0.0.1:5000/bulb/'
updates=[]
prevmsg = ""

def audioHandler(bot, update):
    vfile = bot.getFile(update.message.voice.file_id)
    print vfile.file_path

def cmdHandler(bot, update):
    msg = update.message.text
    chat_id = update.message.chat_id
    if msg == "@home bulb on":
        response = put(url+"color",data={'data':'{"s":255,"r":0,"g":0,"b":0}'}).json()
        bot.sendMessage(chat_id, text="done")
        print response
    if msg == "@home bulb off":
        response = put(url+"color",data={'data':'{"s":0,"r":0,"g":0,"b":0}'}).json()
        bot.sendMessage(chat_id, text="done")
        print response
    if msg == "@home bulb notify":
        response = put(url+"effect",data={'data':'{"s":0,"r":255,"g":255,"b":255,"m":1,"on":15,"off":15}'}).json()
        bot.sendMessage(chat_id, text="done")
        print response
            

def main():
    api = ">>>api key here<<<"
    updater = Updater(api)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler([Filters.text], cmdHandler))
    dp.add_handler(MessageHandler([Filters.voice], audioHandler))
    updater.start_polling()
    updater.idle()


if __name__== "__main__":
    main()
        
