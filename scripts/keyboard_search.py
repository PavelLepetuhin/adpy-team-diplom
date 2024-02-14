from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def keyboard_search():
    keyboard = VkKeyboard()
    keyboard.add_button('Покажи ещё', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('В избранное', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('В чёрный список', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.SECONDARY)

    return keyboard.get_keyboard()