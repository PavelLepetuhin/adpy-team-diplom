from random import randrange

from scripts.keyboard_main import keyboard_main
from scripts.keyboard_search import keyboard_search
from scripts.search_users import search_users
from scripts.vk_find_photo import get_photos_links
from scripts.vk_get_user_info import get_searcher_info


def return_message(personal_token, vk, event, counter, token, user_id):
    age, city_id, sex = get_searcher_info(token, user_id)
    search_result, ids = search_users(personal_token, age, city_id, sex)
    if counter < len(search_result):
        user_id = ids[counter]
        photos = get_photos_links(personal_token, user_id)
        type_ = 'photo'
        owner_id = user_id
        message = search_result[counter]
        attachments = [f'{type_}{owner_id}_{photos[idx][1]}' for idx in range(len(photos))]
        return vk.method('messages.send', {'user_id': event.user_id, 'message': message,
                                    'random_id': randrange(10 ** 7), 'attachment': ','.join(attachments),
                                    'keyboard': keyboard_search()})
    else:
        return vk.method('messages.send', {'user_id': event.user_id, 'message': 'Больше нет подходящих пользователей.',
                                    'random_id': randrange(10 ** 7), 'keyboard': keyboard_main()})