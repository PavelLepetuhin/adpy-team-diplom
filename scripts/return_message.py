from random import randrange

from data_base.select_database import select_all_favorites
from scripts.keyboard_main import keyboard_main
from scripts.keyboard_search import keyboard_search
from scripts.search_users import search_users
from scripts.vk_find_photo import get_photos_links
from scripts.vk_get_user_info import get_current_user_info


def return_message(personal_token, vk, event, counter, current_user_id, search_result, ids):
    if counter < len(search_result):
        user_id = ids[counter]
        photos = get_photos_links(personal_token, user_id)
        type_ = 'photo'
        message = search_result[counter]
        attachments = [f'{type_}{user_id}_{photos[idx][1]}' for idx in range(len(photos))]
        return vk.method('messages.send', {'user_id': current_user_id, 'message': message,
                                    'random_id': randrange(10 ** 7), 'attachment': ','.join(attachments),
                                    'keyboard': keyboard_search()}), user_id, attachments, message
    else:
        return vk.method('messages.send', {'user_id': event.user_id, 'message': 'Больше нет подходящих пользователей.',
                                    'random_id': randrange(10 ** 7), 'keyboard': keyboard_main()})

def return_favorites_list(favorites, vk, count, current_user_id):
    link = favorites[count][0]
    name = favorites[count][1]
    surname = favorites[count][2]
    attachments = [favorites[count][i] for i in range(3,6) if favorites[count][i] != None]
    message = f'{count + 1}. {name} {surname} {link}'
    count += 1
    return vk.method('messages.send', {'user_id': current_user_id, 'message': message,
                                'random_id': randrange(10 ** 7), 'attachment': ','.join(attachments),
                                'keyboard': keyboard_main()})