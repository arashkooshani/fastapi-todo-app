from pydantic import BaseModel,Field
from typing import List,Optional
from datetime import datetime
class TaskBaseSchema(BaseModel):
    title : str = Field(...,max_length=150,min_length=5,description="title of the task")
    description : Optional[str] = Field(None,max_length=500,description="description of the task")
    is_completed : bool = Field(...,description="state of the task")

class TaskCreateSchema(TaskBaseSchema):
    pass

class TaskUpdateSchema(TaskBaseSchema):
    pass

class TaskResponseSchema(TaskBaseSchema):
    id : int = Field(...,description="Unique identifier of the task")
    created_at : datetime = Field(...,description="Creation date and time of the task")
    updated_at : datetime = Field(...,description="Updating date and time of the task")