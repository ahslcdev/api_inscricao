from app.celery.enrollment_tasks.tasks import add_enrollment_task
from app.enrollment_api.routes import router
from tinydb import TinyDB
from app.enrollment_api.schemas import EnrollmentSchema

@router.post("/")
async def create_item(enrollment: EnrollmentSchema):
    try:
        print(type(enrollment.dict()))
        enrollment_dict = enrollment.dict(exclude_unset=True)
        task_id = add_enrollment_task.apply_async(queue='enrollment-queue', args=[enrollment_dict]).id
        # item_id = db.insert(item_dict)
        return task_id
    except Exception as e:
        print("entro pai")
        return f"{e}"
