from bot import bot # bot from bot f[f[f[f[f[]]]]]
from datetime import datetime # а это для логов

def log(message):
    print("<!------!>")
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,message.from_user.last_name,str(message.from_user.id), message.text))
# хуйня выше для логов в консоли
# я знаю, что есть logging, но пошел бы он нахуй

class Telegram: # а я ебу зачем тут класс? я так захотел

    @bot.message_handler(commands = ["start"])
    def command_start(message):
        chat_id = message.chat.id
        bot.send_message(chat_id , "Добро пожаловать {}, user id - {}".format(message.from_user.first_name,chat_id,))
        log(message)
    # команда приветствия и первого запуска f[f[ff[f[f[f]]]]]
    