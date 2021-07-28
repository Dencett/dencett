# import chatbot.keys as cb
import vk_api
from vk_api import bot_longpoll
import random

class Bot:  # TODO РЕР 8 поправьте

    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = bot_longpoll.VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('получено событие')
            self.on_event(event)

    def on_event(self, event):
        if event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.object.text)
            self.api.messages.send(message=event.object.text,
                                   random_id=random.randint(0, 2 ** 20),
                                   peer_id=event.object.peer_id)
        else:
            print('Мы пока не можем обрабатывать событие такого типа: ', event.type)


# if __name__ == '__main__':
#     bot = Bot(cb.group_id, cb.token)
#     bot.run()
