from flask import Flask
from data import db_session
from data.sounds import Sound

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/sounds.sqlite")
    sound = Sound()
    sound.name = 'Удар'
    sound.way = 'static/files_for_data/Удар.mp3'
    sound.category = 'Насилие'
    db_sess = db_session.create_session()
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Что-то пишут на бумаге'
    sound.way = 'static/files_for_data/Что-то пишут на бумаге.mp3'
    sound.category = 'Быт'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Тиканье секундомера'
    sound.way = 'static/files_for_data/Тиканье секундомера.mp3'
    sound.category = 'Приборы'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Стук по дереву'
    sound.way = 'static/files_for_data/Стук по дереву.mp3'
    sound.category = 'Природа'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Сигнализация'
    sound.way = 'static/files_for_data/Сигнализация.mp3'
    sound.category = 'Приборы'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Разбитое стекло'
    sound.way = 'static/files_for_data/Разбитое стекло.mp3'
    sound.category = 'Насилие'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Печать на клавиатуре'
    sound.way = 'static/files_for_data/Печать на клавиатуре.mp3'
    sound.category = 'Приборы'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Перелистывание страницы'
    sound.way = 'static/files_for_data/Перелистывание страницы.mp3'
    sound.category = 'Быт'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Отключение рубильника'
    sound.way = 'static/files_for_data/Отключение рубильника.mp3'
    sound.category = 'Приборы'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Молния на одежде'
    sound.way = 'static/files_for_data/Молния на одежде.mp3'
    sound.category = 'Быт'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Звук выключения'
    sound.way = 'static/files_for_data/Звук выключения.mp3'
    sound.category = 'Приборы'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Звук включения'
    sound.way = 'static/files_for_data/Звук включения.mp3'
    sound.category = 'Приборы'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Зажигание спички'
    sound.way = 'static/files_for_data/Зажигание спички.mp3'
    sound.category = 'Быт'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Выбивание монеты из Super Mario'
    sound.way = 'static/files_for_data/Выбивание монеты из Super Mario.mp3'
    sound.category = 'Видеоигры'
    db_sess.add(sound)
    db_sess.commit()

    sound = Sound()
    sound.name = 'Вода капает'
    sound.way = 'static/files_for_data/Вода капает.mp3'
    sound.category = 'Природа'
    db_sess.add(sound)
    db_sess.commit()


if __name__ == '__main__':
    main()
