import os

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from dotenv import load_dotenv

from crud import (
    get_sections, get_products, get_product_by_name,
)
from db_init import create_db
from keyboard import section_keyboard, product_keyboard

load_dotenv()


def send_message(user_id, message, keyboard=None, attachment=None):
    """Отправляет сообщение пользователю."""
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=get_random_id(),
        keyboard=keyboard,
        attachment=attachment
    )


if __name__ == '__main__':
    create_db()
    vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    upload = vk_api.VkUpload(vk)

    error_msg = None
    sections = get_sections()
    products = get_products()
    work_words = ['start', 'старт', 'Назад'] + sections + products

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = event.text.lower()

            if text == 'start' or text == 'старт':
                keyboard = section_keyboard()
                send_message(
                    user_id=event.user_id,
                    message='Посмотрите на нашу витрину!',
                    keyboard=keyboard.get_keyboard()
                )
            if event.text in sections:
                keyboard = product_keyboard(event.text)
                send_message(
                    user_id=event.user_id,
                    message='Посмотрите на наши товары!',
                    keyboard=keyboard.get_keyboard()
                )
            if event.text in products:
                product = get_product_by_name(event.text)
                photo = upload.photo_messages(product.photo)
                owner_id = photo[0]['owner_id']
                photo_id = photo[0]['id']
                access_key = photo[0]['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                message = (f'Описание товара {product.description}')
                send_message(
                    user_id=event.user_id,
                    message=message,
                    attachment=attachment
                )
            if event.text == 'Назад':
                keyboard = section_keyboard()
                send_message(
                    user_id=event.user_id,
                    message='Назад, так назад',
                    keyboard=keyboard.get_keyboard()
                )
            if text not in work_words and event.text not in work_words:
                if error_msg == 'first_msg':
                    send_message(
                        user_id=event.user_id,
                        message='Думаю вам стоит нажать на кнопки.'
                    )
                if error_msg is None:
                    error_msg = 'first_msg'
                    send_message(
                        user_id=event.user_id,
                        message='Для запуска бота напишите Старт.'
                    )
