"""
Файл с классом конфигурации для приложения.
"""

class Configuration(object):
    # Запускать ли режим отладки
    DEBUG = True
    # Отключение лишнего трекинга
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Подключение к БД
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
