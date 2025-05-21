import logging
from sqlalchemy.orm import Session
from app.core.security import get_password_hash
from app.models.user import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db(db: Session):
    # Create superuser
    user = db.query(User).filter(User.email == "admin@example.com").first()
    if not user:
        user = User(
            email="admin@example.com",
            username="admin",
            hashed_password=get_password_hash("admin"),
            full_name="Administrator",
            is_superuser=True,
        )
        db.add(user)
        db.commit()
        logger.info("Superuser created")
    else:
        logger.info("Superuser already exists") 