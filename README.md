# Flask To-Do List Application

This is a simple To-Do List application built using **Flask** and **SQLite**. It allows users to register, log in, add, update, and delete tasks. Tasks can also be marked as checked or unchecked.

## Features

- User authentication (Login/Logout)
- Add tasks to the to-do list
- Edit tasks directly on the page
- Delete tasks
- Mark tasks as checked/unchecked with checkboxes
- Flash messages for user feedback (e.g., errors or success)

## Technologies Used

- **Flask**: A Python web framework used to build the web application.
- **SQLite**: A lightweight relational database for storing user data and tasks.
- **HTML/CSS**: Basic markup and styling for the front end.
- **JavaScript**: For dynamically handling task interactions like editing and checking tasks.

## Installation

1. Clone the repository to your local machine.
2. Create and activate a virtual environment.
3. Install project dependencies from the `requirements.txt` file.
4. Set up the necessary **config.json** file and **SQLite** database.
5. Run the application with Flask.
6. Open the application in your web browser.

## File Structure

Here’s an overview of the project structure:

- **/static/**
  - **config.json** — Configuration file that contains the secret key.
  - **users.db** — SQLite database file that stores user data and tasks.
  - **index.js** — JavaScript that handles task interactions.
- **/templates/**
  - **index.html** — Main template that displays the to-do list.
  - **login.html** — Login page template.
  - **register.html** — Registration page template.
  - **layout.html** — Layout file that defines the common structure across pages.
- **app.py** — Main Flask application file.
- **requirements.txt** — List of project dependencies.

### **Important Routes**

- **/** — The homepage that shows the list of tasks.
- **/login** — The login page where users can authenticate.
- **/register** — The registration page for new users.
- **/add** — Route to add new tasks to the list.
- **/update/<int:id>** — Route to update tasks (edit the text or mark as checked).
- **/delete/<int:id>** — Route to delete tasks.

## Usage

1. **Register**:
   Navigate to the **/register** route to create a new account. Fill out the registration form to create your user credentials.

2. **Login**:
   Use the **/login** route to log into your account. After logging in, you’ll be redirected to the main to-do list page where you can manage your tasks.

3. **Adding Tasks**:
   Once logged in, you can add tasks to your to-do list by typing them into the input field and clicking "Add".

4. **Editing Tasks**:
   You can edit any task directly in the list by clicking the pencil icon. This will allow you to change the task text.

5. **Deleting Tasks**:
   You can delete tasks by clicking the trash icon next to the task you want to remove.

6. **Marking Tasks as Completed**:
   Each task has a checkbox. You can check or uncheck the box to mark a task as completed or pending.

## Flash Messages

The application uses Flask's `flash` system to display feedback to the user:

- If an error occurs (e.g., missing input or failed task operation), the error will be displayed at the top of the page.
- Flash messages appear in a dedicated area with a temporary message (like "Task added successfully!" or "An error occurred while adding the task.").
