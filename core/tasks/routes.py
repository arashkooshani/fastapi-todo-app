from fastapi import APIRouter

router=APIRouter(tags=["tasks"],prefix="/todo")

@router.get('/tasks')
def retrieve_tasks_list():
    return []

@router.get('/tasks/{task_id}')
def retrieve_tasks_detail(task_id : int):
    return []