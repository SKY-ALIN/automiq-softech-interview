"""
Файл с классом конфигурации для приложения.
"""

class Configuration():
    # Запускать ли режим отладки
    DEBUG = True
    # Отключение лишнего трекинга
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Подключение к БД
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://test_user:password@localhost/automiq'
