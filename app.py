from flask import Flask
from flask_cors import CORS

import routes
from models import *
from models.notification import Notification
from services.notification_service import EmailNotificationService


def create_app():
    app = Flask(__name__)
    app.json.ensure_ascii = False
    app.json.sort_keys = False
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:1234@localhost/stride'

    db.init_app(app)

    [app.register_blueprint(blueprint) for blueprint in routes.blueprints]

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=80)
