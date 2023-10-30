from app import db, create_app
from app.models.user import User

app = create_app()


def setup_database():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    setup_database()
