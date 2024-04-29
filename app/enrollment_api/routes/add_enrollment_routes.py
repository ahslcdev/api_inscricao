from fastapi import status, HTTPException
from app.celery.enrollment_tasks.tasks import add_enrollment_task
from app.enrollment_api.error_messages import ErrorMessageBadRequest
from app.enrollment_api.exceptions import InvalidAge, InvalidCPF
from app.enrollment_api.routes import router
from app.enrollment_api.schemas import EnrollmentSchema

@router.post(
    "/",
    responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":ErrorMessageBadRequest
        },
        status.HTTP_200_OK:{
            "content": {
                "application/json": {
                    "example": 
                        {
                            "message": "Sua solicitação de inscrição foi confirmada,"
                                       "para checar o status da solicitação,"
                                       "voce pode consultar pelo ID: 1234"
                        }
                }
            },
        }
    }
)
async def create_item(enrollment: EnrollmentSchema):
    """
    Este route é responsável por receber os dados da inscrição
    e chamar a task responsável pela criação no banco de dados.
    """
    try:
        enrollment_dict = enrollment.dict(exclude_unset=True)
        task_id = add_enrollment_task.apply_async(queue='enrollment-queue', args=[enrollment_dict]).id
        task_message = {
            "message":"Sua solicitação de inscrição foi confirmada," 
                      "para checar o status da solicitação,"
                      f"voce pode consultar pelo ID: {task_id}" 
        }
    except (Exception, InvalidAge, InvalidCPF) as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            str(e)
        )
    return task_message