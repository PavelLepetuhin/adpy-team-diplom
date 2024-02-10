import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


def keyboard_main():
    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Найди мне пару', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Мои избранные', color=VkKeyboardColor.SECONDARY)

    return keyboard.get_keyboard()