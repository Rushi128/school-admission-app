
# School Admission Application

Welcome to the School Admission Application! This web application is designed to facilitate the registration and login process for students, as well as provide administrative functions for teachers. With this application, teachers can manage student registrations, allocate roll numbers, and perform various administrative tasks.

## Features

- User Registration: Students can create an account by providing their details, including their name, email, and password.

- User Login: Registered students can log in securely using their email and password.

- Administrator Access: Teachers have administrative privileges and can manage student registrations, assign roll numbers, and perform other administrative tasks.

- Student Profile: Each student has a personal profile displaying their registered information and roll number (allocated by the administrator).

- User Roles: The application distinguishes between students and teachers, providing appropriate access and functionality based on their roles.

## Technologies Used

- Python: The project is developed using the Python programming language.

- Flask: Flask, a lightweight web framework, is used for building the application.

- SQLite: The SQLite database is utilized for storing user information and roll numbers.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Rushi128/school-admission-app.git
```

2. Change to the project directory:

```bash
cd school-admission-app
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- For Windows:

```bash
venv\Scripts\activate
```

- For macOS/Linux:

```bash
source venv/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Set up the database:

```bash
flask db init
flask db migrate
flask db upgrade
```

7. Start the application:

```bash
flask run
```

8. Open your web browser and visit `http://localhost:5000` to access the School Admission Application.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact

For any inquiries or further information, please contact [Rushikesh Thorat] via email at [rushithorat128@gmail.com].

---
