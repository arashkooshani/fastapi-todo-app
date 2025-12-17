from fastapi import APIRouter,Path,Depends,HTTPException,Query
from .schemas import *
from .models import TaskModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List
from fastapi.responses import JSONResponse
router=APIRouter(tags=["tasks"],prefix="/todo")

@router.get('/tasks',response_model=List[TaskResponseSchema])
def retrieve_tasks_list(
        completed: bool = Query(None,description="filter tasks on whether they are completed or not"),
        limit: int = Query(10,gt=0,le=50),
        offset: int = Query(0,ge=0),
        db : Session = Depends(get_db)):
    query=db.query(TaskModel)
    if completed is not None:
        query=query.filter_by(is_completed=completed)
    return query.limit(limit).offset(offset).all()

@router.get('/tasks/{task_id}',response_model=TaskResponseSchema)
def retrieve_tasks_detail(
        task_id : int = Path(..., gt=0),
        db : Session = Depends(get_db)):
    query= db.query(TaskModel).filter_by(id=task_id).one_or_none()
    if not query:
        raise HTTPException(status_code=404,detail="Task not found")
    return query

@router.post('/tasks')
def create_task(request : TaskCreateSchema,db : Session = Depends(get_db)):
    task_object=TaskModel(**request.model_dump())
    db.add(task_object)
    db.commit()
    db.refresh(task_object)
    return task_object

@router.put('/tasks/{task_id}',response_model=TaskResponseSchema)
def update_task(request: TaskUpdateSchema,task_id : int = Path(..., gt=0),db : Session = Depends(get_db)):
    task_object = db.query(TaskModel).filter_by(id=task_id).first()
    if not task_object:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in request.model_dump().items():
        setattr(task_object, key, value)
    db.commit()
    db.refresh(task_object)
    return task_object

@router.delete('/tasks/{task_id}')
def delete_task(task_id : int = Path(..., gt=0), db : Session = Depends(get_db)):
    task_object = db.query(TaskModel).filter_by(id=task_id).first()
    if not task_object:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task_object)
    db.commit()
    return JSONResponse(status_code=200, content="Task removed successfully")