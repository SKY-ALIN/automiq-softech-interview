"""
Файл с маршрутами приложения.
"""

from flask import render_template, redirect, url_for, request

from app import app, db
from models import Product, Version

@app.route('/')
def products():
    """Главный маршрут. Тут можно увидеть список продуктов компании
    и их версии.
    """

    products_list = Product.query.all()
    return render_template('products.html', products=products_list)

@app.route('/<version_id>/')
def version(version_id):
    """Маршрут дляпросмотра конкретной версии (version_id) конкретного
    продукта и взаимосвязи с другими.
    """

    version_object = Version.query.filter(Version.id == version_id).first()
    return render_template('version.html', version=version_object)
