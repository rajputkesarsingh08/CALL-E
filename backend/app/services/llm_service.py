import json

import requests

from app.config import settings
from app.schemas.call import CallPlan
from app.schemas.call import CallPlanRequest


def create_call_plan(
    request: CallPlanRequest
) -> dict:

    if not settings.LLM_API_KEY:

        return {

            "objective":
                request.purpose,

            "target":
                request.target,

            "questions": [
                "Can you provide the requested information?",
                "Is there anything else the student needs to do?",
                "What is the next step?"
            ],

            "tone":
                "professional and polite",

            "success_criteria": [
                "requested information obtained",
                "next action obtained",
            ],
        }


    system_prompt = """
You are a call-planning assistant.

Convert a student's phone task into
structured JSON.

Return ONLY JSON with:

objective
target
questions
tone
success_criteria

Do not invent facts.
Keep questions concise.
The agent must identify itself as an AI assistant
when appropriate.
Never impersonate a person.
"""


    user_prompt = f"""
Target:
{request.target}

Purpose:
{request.purpose}

Additional instructions:
{request.additional_instructions}

Preferred outcome:
{request.preferred_outcome}
"""


    url = (
        settings.LLM_BASE_URL.rstrip("/")
        + "/chat/completions"
    )


    payload = {

        "model":
            settings.LLM_MODEL,

        "messages": [

            {
                "role": "system",
                "content": system_prompt,
            },

            {
                "role": "user",
                "content": user_prompt,
            },
        ],

        "temperature": 0.2,
    }


    response = requests.post(
        url,

        headers={
            "Authorization":
                f"Bearer {settings.LLM_API_KEY}",

            "Content-Type":
                "application/json",
        },

        json=payload,

        timeout=45,
    )


    response.raise_for_status()


    data = response.json()


    content = (
        data["choices"][0]
        ["message"]["content"]
    )


    parsed = json.loads(content)


    validated = CallPlan.model_validate(
        parsed
    )


    return validated.model_dump()