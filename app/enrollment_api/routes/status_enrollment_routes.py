from fastapi import status, HTTPException
from app.enrollment_api.error_messages import ErrorMessageBadRequest
from app.enrollment_api.routes import router
from app.enrollment_api.service import EnrollmentService

@router.get(
    "/check-status/{id}/",
    responses={
        status.HTTP_400_BAD_REQUEST:{
            "model":ErrorMessageBadRequest
        },
        status.HTTP_200_OK:{
            "content": {
                "application/json": {
                    "example": 
                        {
                            "message": "Inscrição Aprovada."
                        }
                }
            },
        }
    }
)
async def check_status(id: str):
    try:
        status = EnrollmentService().get_status_enrollment(id)
        message = {"message":"Inscrição pendente"}
        if status:
            message['message'] = 'Inscrição aprovada'
    except Exception as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            str(e)
        )
    return message
