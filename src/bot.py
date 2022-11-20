import telebot # telebot, ахахахахахахха
import toml # работа с toml конфигом, иди нахуй json
conf = toml.load("config.toml") # загружаем сам конфиг
bot = telebot.TeleBot(conf["telegram_settings"]["api_token"]) # bot f[f[f[f[f[f]]]]]
def startup():
    print("Test telegram bot!") # ну крч это да!
    bot.polling(non_stop=True) # запуск анальной бестии
startup()