# Django Recipe Project

This repository contains a Django web application for managing and sharing recipes. The application allows users to create, edit, delete, and view recipes.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#Author)
- [Contact](#contact)

## Project Overview

The Django Recipe Project is designed to provide a platform for users to manage and share their favorite recipes. The application is built using the Django framework and follows best practices for web development.

## Features

- User authentication (signup, login, logout)
- Create, edit, and delete recipes
- View a list of all recipes
- View detailed information about each recipe

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/itz-shakil-92/django_receipe_project.git
    ```

2. Navigate to the project directory:
    ```bash
    cd django_receipe_project
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the admin interface:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

To use the application, follow these steps:

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Sign up for a new account or log in if you already have an account.
3. Start creating, editing, and viewing recipes.

## Author
- [Shakil Kathat](https://www.github.com/itz-shakil-92)

## Contact
If you have any questions or need further assistance, please feel free to contact us at shakilkathat5603@gmail.com
