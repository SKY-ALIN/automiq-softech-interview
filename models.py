"""
Файл с моделями приложения.
"""

from app import db

class Product(db.Model):
    """Модель описывающая список продуктов компании. К конкретному продукту уже
    привязываются отдельные версии продукта (они хранятся в модели Version)
    """

    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    versions = db.relationship('Version', lazy=True, backref='product')

# Таблица описывающая связи между артефактами
VersionRelationship = db.Table('VersionRelationship',
    db.Column('first_version_id', db.Integer, db.ForeignKey('versions.id')),
    db.Column('second_version_id', db.Integer, db.ForeignKey('versions.id'))
)

class Version(db.Model):
    """Модель описывающая отдельную версию отдельного продукта."""

    __tablename__ = 'versions'
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(255))
    description = db.Column(db.Text)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    dependences = db.relationship('Version', secondary=VersionRelationship,
                                  primaryjoin=VersionRelationship.c.first_version_id == id,
                                  secondaryjoin=VersionRelationship.c.second_version_id == id,
                                  backref='side_dependences')
