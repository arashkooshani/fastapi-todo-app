from fastapi import APIRouter,Path,Depends,HTTPException
from .schemas import *
from .models import TaskModel
from sqlalchemy.orm import Session
from core.database import get_db


router=APIRouter(tags=["tasks"],prefix="/todo")

@router.get('/tasks')
def retrieve_tasks_list():
    return []

@router.get('/tasks/{task_id}')
def retrieve_tasks_detail(task_id : int = Path(..., gt=0)):
    return []

@router.post('/tasks')
def create_task():
    return []

@router.put('/tasks/{task_id}')
def update_task(task_id : int = Path(..., gt=0)):
    return []