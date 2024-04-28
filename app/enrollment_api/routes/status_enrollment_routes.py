from app.enrollment_api.routes import router
from app.enrollment_api.service import EnrollmentService

@router.get("/check-status/{id}/")
async def check_status(id: str):
    try:
        status = EnrollmentService().get_status_enrollment(id)
        if status:
            return 'Inscrição aprovada'
        else:
            return 'Inscrição Pendente'
        # print(type(enrollment.dict()))
        # enrollment_dict = enrollment.dict(exclude_unset=True)
        # task_id = add_enrollment_task.apply_async(queue='enrollment-queue', args=[enrollment_dict]).id
        # # item_id = db.insert(item_dict)
        # return task_id
    except Exception as e:
        print("entro pai")
        return f"{e}"
