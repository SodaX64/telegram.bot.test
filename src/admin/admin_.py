#тут все как и у клиентв, только нужен доступ к конфигу тк как админку делать?
from bot import bot
from datetime import datetime
from bot import conf

def log(message):
    print("<!------!>")
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,message.from_user.last_name,str(message.from_user.id), message.text))


class Telegram:
    
    @bot.message_handler(commands= ["admin"])
    def command_start(message):
        chat_id = message.chat.id
        if str(chat_id) == conf["telegram_settings"]["admin_chat_id"]:
            bot.send_message(chat_id , "Дарова {}, мой повелитель!".format(message.from_user.first_name))
        else:
            bot.send_message(chat_id , "Ты не админ!")
        log(message)
        