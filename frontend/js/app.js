const API_BASE =
    window.CAMPUSCONNECT_API || "http://localhost:8000";


/* -----------------------------------
   MOBILE NAVIGATION
----------------------------------- */

const menuButton =
    document.getElementById("menuBtn");

const navLinks =
    document.getElementById("navLinks");


if (menuButton && navLinks) {

    menuButton.addEventListener("click", () => {

        if (navLinks.style.display === "flex") {

            navLinks.style.display = "none";

            return;
        }

        navLinks.style.display = "flex";

        navLinks.style.position = "absolute";
        navLinks.style.top = "120px";
        navLinks.style.left = "12px";
        navLinks.style.right = "12px";

        navLinks.style.flexDirection = "column";

        navLinks.style.padding = "18px";

        navLinks.style.background = "white";

        navLinks.style.border =
            "1px solid #ddd9ce";

        navLinks.style.borderRadius =
            "18px";

        navLinks.style.zIndex = "999";
    });
}


/* -----------------------------------
   SCROLL TO CALL FORM
----------------------------------- */

function scrollToCallForm() {

    const section =
        document.getElementById("new-call");

    if (!section) {
        return;
    }

    section.scrollIntoView({
        behavior: "smooth"
    });
}


/* -----------------------------------
   PHONE VALIDATION
----------------------------------- */

function isValidPhoneNumber(phone) {

    return /^\+[1-9]\d{7,14}$/.test(
        phone
    );
}


/* -----------------------------------
   CALL FORM
----------------------------------- */

const callForm =
    document.getElementById("callForm");

const formMessage =
    document.getElementById("formMessage");


if (callForm) {

    callForm.addEventListener(
        "submit",
        async function (event) {

            event.preventDefault();

            const target =
                document.getElementById("target")
                    .value
                    .trim();

            const phone =
                document.getElementById("phone")
                    .value
                    .trim();

            const purpose =
                document.getElementById("purpose")
                    .value
                    .trim();

            const instructions =
                document.getElementById("instructions")
                    .value
                    .trim();

            const outcome =
                document.getElementById("outcome")
                    .value
                    .trim();


            if (!target || !phone || !purpose) {

                showMessage(
                    "Please complete all required fields.",
                    true
                );

                return;
            }


            if (!isValidPhoneNumber(phone)) {

                showMessage(
                    "Use an E.164 phone number, for example +919876543210.",
                    true
                );

                return;
            }


            showMessage(
                "Preparing your AI call plan..."
            );


            try {

                const response =
                    await fetch(
                        `${API_BASE}/api/calls/plan`,
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({

                                phone_number:
                                    phone,

                                target:
                                    target,

                                purpose:
                                    purpose,

                                additional_instructions:
                                    instructions ||
                                    "Be polite, concise and identify as an AI assistant when appropriate.",

                                preferred_outcome:
                                    outcome ||
                                    "Get the useful answer and the next action for the student."
                            })
                        }
                    );


                const data =
                    await response
                        .json()
                        .catch(() => ({}));


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Unable to create a call plan."
                    );
                }


                showMessage(
                    "Call plan created successfully."
                );


                console.log(
                    "CALL PLAN:",
                    data
                );

                displayCallPlan(data);

            } catch (error) {

                console.error(error);

                showMessage(
                    error.message ||
                    "Backend connection failed.",
                    true
                );
            }
        }
    );
}


/* -----------------------------------
   SHOW MESSAGE
----------------------------------- */

function showMessage(
    message,
    error = false
) {

    if (!formMessage) {
        return;
    }

    formMessage.textContent =
        message;

    formMessage.style.color =
        error
            ? "#ff9b96"
            : "#aaa";
}


/* -----------------------------------
   DISPLAY CALL PLAN
----------------------------------- */

function displayCallPlan(plan) {

    console.log(
        "Objective:",
        plan.objective
    );

    console.log(
        "Questions:",
        plan.questions
    );

    console.log(
        "Tone:",
        plan.tone
    );

    console.log(
        "Success criteria:",
        plan.success_criteria
    );
}
document.addEventListener("contextmenu", function (event) {
    event.preventDefault();
});
document.addEventListener("contextmenu", function (event) {
    event.preventDefault();
});

document.addEventListener("keydown", function (event) {

    // F12
    if (event.key === "F12") {
        event.preventDefault();
    }

    // Ctrl + Shift + I
    if (
        event.ctrlKey &&
        event.shiftKey &&
        event.key.toLowerCase() === "i"
    ) {
        event.preventDefault();
    }

    // Ctrl + Shift + J
    if (
        event.ctrlKey &&
        event.shiftKey &&
        event.key.toLowerCase() === "j"
    ) {
        event.preventDefault();
    }

    // Ctrl + U
    if (
        event.ctrlKey &&
        event.key.toLowerCase() === "u"
    ) {
        event.preventDefault();
    }
});

/* -----------------------------------
   LOAD CALL HISTORY
----------------------------------- */

async function loadCallHistory() {

    try {

        const response =
            await fetch(
                `${API_BASE}/api/calls`
            );

        if (!response.ok) {
            return;
        }

        const calls =
            await response.json();

        console.log(
            "Call history:",
            calls
        );

    } catch (error) {

        console.error(
            "History loading failed:",
            error
        );
    }
}


/* -----------------------------------
   INITIALIZE
----------------------------------- */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadCallHistory();

    }
);
