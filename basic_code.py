from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from scripts.keyboard_main import keyboard_main
from scripts.return_message import return_message

token = 'vk1.a.7MO6NuCs4vEa4oUzmGpN3OQ6TmGMMplJn0yc7fnYBWPlYabofFDIE5aU7YxJN-xP4F5iDhzhq9jkorNbtzvc8vTw2txN7bCSrwKulpbbUO-gLWqlxljZpJwaCp8ByKgDCOe71gmd2QSsJLoJytRlTpbGuLfs6h6ivT5RW4kqQ3ndVqKiL85to2YATtvRmmcjKpIPVMXlA1zZA8yzOyFJMg'
personal_token = 'vk1.a.zSlO9ah3SvzMAfImk4CL4NxxKvrLzD_wSQHLS2Eg9TwJPUXZm12kZBsN3_MCcF1AiWUgwCdvBS8Ryigbjf0XeSkoR4gLIG2EBeApLFStCSSqlgYvAjGAPBUVpZM23mA3Ruq9O5ZktRmIyAasfnjWLE8cBwCZ6ICzA_QKUwT7299OHyAPxheVhVyMv_Sv5igpwC_iNSyYSFdv1G4U8wQF-Q'

# token = input('Token: ')
# personal_token = input('Personal token: ')

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),
                                'keyboard': keyboard_main()})

counter = 0
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "Привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")

            elif request == "Найди мне пару":
                return_message(personal_token, vk, event, counter, token, event.user_id)

            elif request == 'Покажи ещё':
                counter += 1
                return_message(personal_token, vk, event, counter, token, event.user_id)

            elif request == 'В чёрный список':
                pass

            elif request == 'Мои избранные':
                pass

            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
