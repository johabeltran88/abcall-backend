from flask import Flask
from src.config.database import init_db, db
from src.controllers.health_controller import health_bp
from src.controllers.user_controller import user_bp

app = Flask(__name__)
init_db(app)

app.register_blueprint(user_bp)
app.register_blueprint(health_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
