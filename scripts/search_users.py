import vk_api

from data_base.select_database import select_blacklist


def search_users(personal_token, age, city_id, sex, current_user_id):
    vk = vk_api.VkApi(token=personal_token)
    if sex == 1:
        sex = 2
    if sex == 2:
        sex = 1
    vk_search_users = vk.method('users.search', {'city_id': city_id, 'age_from': 18, 'age_to': age, 'sex': sex, 'has_photo': 1})
    search_result = vk_search_users.get('items')
    users = []
    ids = []
    for idx in range(len(search_result)):
        id_ = search_result[idx].get('id')
        check_in_blacklist = select_blacklist(current_user_id, id_)
        if check_in_blacklist != None:
            continue
        else:
            name = search_result[idx].get('first_name') + ' ' + search_result[idx].get('last_name')
            user = f"{name} https://vk.com/id{id_}"
            users.append(user)
            ids.append(id_)
    return users, ids