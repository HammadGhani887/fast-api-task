import uvicorn
from app.db.session import SessionLocal, engine
from app.db.init_db import init_db
from app.models import user, task, template

def init() -> None:
    # Create tables
    user.Base.metadata.create_all(bind=engine)
    task.Base.metadata.create_all(bind=engine)
    template.Base.metadata.create_all(bind=engine)
    
    # Initialize database
    db = SessionLocal()
    init_db(db)

if __name__ == "__main__":
    init()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 