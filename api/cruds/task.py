from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema


def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    print("Task to be added: {task}")  # 追加するタスクを表示
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
