"""
Файл с маршрутами приложения.
"""

from flask import render_template

from app import app
from models import Product, Version

@app.route('/')
def products():
    """Главный маршрут. Тут можно увидеть список продуктов компании
    и их версии.
    """

    products_list = Product.query.all()
    return render_template('products.html', products=products_list)

@app.route('/all/')
def all():
    """Маршрут для просмотра всех продуктов, версий и зависимостей
    (как в письме)
    """

    products_list = Product.query.all()
    return render_template('all.html', products=products_list)

@app.route('/<version_id>/')
def version(version_id):
    """Маршрут дляпросмотра конкретной версии (version_id) конкретного
    продукта и взаимосвязи с другими.
    """

    version_object = Version.query.filter(Version.id == version_id).first_or_404()
    return render_template('version.html', version=version_object)
