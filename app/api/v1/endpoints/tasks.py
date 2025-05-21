from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.deps import get_db, get_current_active_user
from app.schemas.task import Task, TaskCreate
from app.models.task import Task as TaskModel
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Task)
def create_task(
    *,
    db: Session = Depends(get_db),
    task_in: TaskCreate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create new task.
    """
    task = TaskModel(
        title=task_in.title,
        description=task_in.description,
        user_id=current_user.id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/", response_model=List[Task])
def read_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve tasks for current user.
    """
    tasks = db.query(TaskModel).filter(TaskModel.user_id == current_user.id).offset(skip).limit(limit).all()
    return tasks

@router.get("/{task_id}", response_model=Task)
def read_task(
    *,
    db: Session = Depends(get_db),
    task_id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get task by ID.
    """
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return task 