const checkboxes = document.getElementsByClassName("checkbox-input");

for (let checkbox of checkboxes) {
    if (checkbox.checked) {
        document.getElementById("task-text-" + checkbox.getAttribute("id")).style.textDecoration = "line-through";
    }

    checkbox.addEventListener("change", () => {
        if (checkbox.checked) {
            document.getElementById("task-text-" + checkbox.getAttribute("id")).style.textDecoration = "line-through";
            saveStatus(id, 1, "Check");
        } else {
            document.getElementById("task-text-" + checkbox.getAttribute("id")).style.textDecoration = "none";
            saveStatus(id, 0, "Check");
        }
    })
}

function updateTask(id) {
    const taskText = document.getElementById("task-text-" + id);
    const editTask = document.getElementById("task-edit-" + id);

    taskText.style.display = "none";
    editTask.style.display = "inline-block"

    editTask.value = taskText.textContent;

    editTask.focus();

    editTask.addEventListener("blur", () => {
        saveTask(id);
    });

    editTask.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            saveTask(id);
        }
    });
}

async function saveTask(id) {
    const taskText = document.getElementById("task-text-" + id);
    const editTask = document.getElementById("task-edit-" + id);

    const text = editTask.value;

    saveStatus(id, text, "Task")

    taskText.textContent = text;
    taskText.style.display = "inline-block";
    editTask.style.display = "none";

    const blurListener = () => saveTask(id);
    const keydownListener = (event) => {
        if (event.key === "Enter") {
            saveTask(id);
        }
    };

    editTask.removeEventListener("blur", blurListener);
    editTask.removeEventListener("keydown", keydownListener);
}

async function saveStatus(id, field, type) {
    let json;

    if (type === "Task") {
        json = { text: field }
    } else {
        json = { checked: field }
    }

    try {
        await fetch("/update/" + id, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(json)
        });
    } catch (error) {
        alert("Error saving task: " + error.message);
    }
}