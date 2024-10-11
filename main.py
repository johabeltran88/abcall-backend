from flask import Flask
from src.config.database import init_db, db
from src.controllers.agent_controller import agent_bp
from src.controllers.health_controller import health_bp

app = Flask(__name__)
init_db(app)

app.register_blueprint(agent_bp)
app.register_blueprint(health_bp)


if __name__ == '__main__':
    with app.app_context():
        print("crea db y tablas")
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
