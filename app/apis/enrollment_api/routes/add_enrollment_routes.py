from fastapi import status, HTTPException
from app.apis.enrollment_api.tasks import add_enrollment_task
from app.apis.enrollment_api.error_messages import ErrorMessageBadRequest
from app.apis.enrollment_api.exceptions import InvalidAge, InvalidCPF
from app.apis.enrollment_api.routes import router
from app.apis.enrollment_api.schemas import EnrollmentSchema
from app.apis.enrollment_api.utils import validate_age, validate_cpf

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
                                       "voce pode consultar pelo ID: 1234",
                            "id": "1234"
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
        enrollment_dict = enrollment.model_dump(exclude_unset=True)
        if not validate_cpf(enrollment_dict.get('cpf')):
            raise InvalidCPF("CPF inválido")
        validate_age(enrollment_dict.get('age'))
        task_id = add_enrollment_task.apply_async(queue='enrollment-queue', args=[enrollment_dict]).id
        task_message = {
            "message": "Sua solicitação de inscrição foi confirmada," 
                      "para checar o status da solicitação,"
                      f"voce pode consultar pelo ID: {task_id}",
            "id": task_id
        }
    except (Exception, InvalidAge, InvalidCPF) as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return task_message