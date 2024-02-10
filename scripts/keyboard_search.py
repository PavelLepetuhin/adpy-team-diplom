import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


def keyboard_search():
    keyboard = VkKeyboard(inline=True)
    keyboard.add_button('Покажи ещё', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('В избранное', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('В чёрный список', color=VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()