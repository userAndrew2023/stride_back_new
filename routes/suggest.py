from flask import Blueprint, request, jsonify

from services.suggest_service import YandexMapSuggestService

suggestBlueprint = Blueprint('suggest', __name__, url_prefix='/suggest')


@suggestBlueprint.route('/', methods=['GET'])
def suggest():
    text = request.args.get('text')
    suggestService = YandexMapSuggestService()

    return jsonify(suggestService.getSuggestions(text))
