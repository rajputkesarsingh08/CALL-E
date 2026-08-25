from typing import Any


def extract_call_result(
    calle_response: dict
) -> dict:

    result = (
        calle_response.get(
            "result"
        )
        or {}
    )

    transcript = (
        calle_response.get(
            "transcript"
        )
        or []
    )

    summary = (
        result.get(
            "summary"
        )
        or "No summary available."
    )

    confidence = (
        result.get(
            "confidence"
        )
    )

    return {

        "status":
            calle_response.get(
                "status"
            ),

        "summary":
            summary,

        "confidence":
            confidence,

        "evidence":
            result.get(
                "evidence",
                []
            ),

        "transcript":
            transcript,
    }