from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from crud import get_products_by_section_name, get_sections


def product_keyboard(name):
    """Создаёт клавиатуру для товара."""
    keyboard = VkKeyboard()
    products = get_products_by_section_name(name)
    for product in products:
        keyboard.add_button(product.name, VkKeyboardColor.PRIMARY)
        if len(product.name) > 10:
            keyboard.add_line()
    keyboard.add_button('Назад', VkKeyboardColor.NEGATIVE)
    return keyboard


def section_keyboard():
    """Создаёт клавиатуру для раздела."""
    keyboard = VkKeyboard()
    sections = get_sections()
    for section in sections:
        keyboard.add_button(section, VkKeyboardColor.PRIMARY)
        if len(section) > 10:
            keyboard.add_line()
    return keyboard
