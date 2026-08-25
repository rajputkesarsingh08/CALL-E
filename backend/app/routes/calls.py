import json

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.call import Call

from app.schemas.call import CallPlan
from app.schemas.call import CallPlanRequest

from app.services.llm_service import create_call_plan
from app.services.calle_service import create_calle_call


router = APIRouter(
    prefix="/calls",
    tags=["Calls"]
)


@router.post("/plan")
def plan_call(
    request: CallPlanRequest
):

    try:

        plan = create_call_plan(
            request
        )

        return plan

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@router.post("/start")
def start_call(
    request: CallPlanRequest,
    db: Session = Depends(get_db)
):

    try:

        plan = create_call_plan(
            request
        )

        calle_call = create_calle_call(
            phone_number=request.phone_number,
            plan=plan,
        )

        call = Call(

            calle_call_id=
                calle_call["id"],

            phone_number=
                request.phone_number,

            target=
                request.target,

            purpose=
                request.purpose,

            status=
                "CALLING",
        )

        db.add(call)
        db.commit()
        db.refresh(call)

        return {

            "id": call.id,

            "calle_call_id":
                call.calle_call_id,

            "status":
                call.status,

            "plan":
                plan,
        }

    except Exception as exc:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@router.get("")
def get_calls(
    db: Session = Depends(get_db)
):

    calls = (
        db.query(Call)
        .order_by(
            Call.created_at.desc()
        )
        .all()
    )

    return calls


@router.get("/{call_id}")
def get_call(
    call_id: int,
    db: Session = Depends(get_db)
):

    call = (
        db.query(Call)
        .filter(
            Call.id == call_id
        )
        .first()
    )

    if not call:

        raise HTTPException(
            status_code=404,
            detail="Call not found."
        )

    return call