from flask import Blueprint, request, jsonify
from models import db
from models.category import Category

categoriesBlueprint = Blueprint('categories', __name__, url_prefix='/categories')


@categoriesBlueprint.route('/', methods=['GET'])
def get_categories():
    return jsonify({'categories': Category.query.all()})


@categoriesBlueprint.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    return jsonify(Category.query.get_or_404(category_id))


@categoriesBlueprint.route('/', methods=['POST'])
def add_category():
    data = request.get_json()
    new_category = Category(**data)
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully!'})


@categoriesBlueprint.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    data = request.get_json()
    category.update(data)  # Assuming Category has an update method
    db.session.commit()
    return jsonify({'message': 'Category updated successfully!'})


@categoriesBlueprint.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    db.session.delete(Category.query.get_or_404(category_id))
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'})
