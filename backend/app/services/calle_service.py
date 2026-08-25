import requests

from app.config import settings


def create_calle_call(
    phone_number: str,
    plan: dict,
) -> dict:

    if not settings.CALL_E_API_KEY:

        raise RuntimeError(
            "CALL_E_API_KEY is not configured."
        )


    instructions = f"""
You are CampusConnect AI,
an AI phone assistant helping a student.

You are NOT the student.
Do not impersonate a person.
Identify yourself as an AI assistant
when appropriate or required.

Target:
{plan["target"]}

Objective:
{plan["objective"]}

Questions:
{chr(10).join(plan["questions"])}

Tone:
{plan["tone"]}

Success criteria:
{chr(10).join(plan["success_criteria"])}

Be polite and concise.

Ask only information relevant
to the task.

Do not collect unnecessary sensitive
personal information.

Do not make commitments on behalf
of the student.

Once the task is complete,
politely end the call.
"""


    url = (
        settings.CALL_E_BASE_URL.rstrip("/")
        + "/v1/calls"
    )


    payload = {

        "to":
            phone_number,

        "instructions":
            instructions,
    }


    response = requests.post(

        url,

        headers={

            "Authorization":
                f"Bearer {settings.CALL_E_API_KEY}",

            "Content-Type":
                "application/json",
        },

        json=payload,

        timeout=45,
    )


    response.raise_for_status()


    return response.json()