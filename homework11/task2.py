# ======== additional tasks=======

# ==== task 3 ====
class MyStr:
    def __init__(self, str):
        self.str = str
        print(str.upper())
MyStr("hello")

# ==== task 4 ====

# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         return self.name.lower() == other
# name1 = User("dania")
# name2 = User("DANIA")
# name3 = User("Denis")
# print(name1 == name2)

# ==== task 5 ====


# class Bot(object):
#     def __init__(self, name):
#         self.name = name
#
#     def send_name(self):
#         print(self.name)
#
#     def send_message(self, message):
#         print(message)
#
# new_bot = type("Bot", (object,),
#            {"__init__": Bot.__init__,
#             "say_name": Bot.send_name,
#             "send_message": Bot.send_message})
#
# class TelegramBot(Bot):
#     def __init__(self, name):
#         super().__init__(name)
#         self.url = None
#         self.chat_id = None
#
#     def set_url(self, url):
#         self.url = url
#
#     def set_chat_id(self, chat_id):
#         self.chat_id = chat_id
#
#     def send_message(self, message):
#         print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")
#
# new_telegrambot = type("TelegramBot", (Bot,),
#                     {"__init__": TelegramBot.__init__,
#                     "set_url": TelegramBot.set_url,
#                     "set_chat_id": TelegramBot.set_chat_id,
#                     "send_message": TelegramBot.send_message})
#
#
# some_bot = Bot('John')
# some_bot.send_name()
# some_bot.send_message("Hello")
#
# telegram_bot = TelegramBot("TG")
# telegram_bot.send_name()
# telegram_bot.send_message('Hello')
# telegram_bot.set_chat_id(1)
# telegram_bot.send_message('Hello')
