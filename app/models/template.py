from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.session import Base

class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rename = Column(String)
    is_active = Column(Boolean, default=True)
    template_data = Column(JSON)  # Stores the entire template structure
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class TemplateSubmission(Base):
    __tablename__ = "template_submissions"

    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("templates.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    submission_data = Column(JSON)  # Stores the submitted form data
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 