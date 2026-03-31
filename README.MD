# Student Manager System

## Project Overview
A command-line based student management system built in Python that allows users to manage student records with data persistence via CSV files. This project demonstrates CRUD operations, input validation, and file handling.

**Developed by:** Jose David Romero Lara  
**Language:** Python 3.10+  
**License:** MIT (assumed)

## Features
- **Data Persistence**: Automatically loads and saves student data to/from a CSV file.
- **Add Students**: Register new students with unique IDs, names, ages, courses, and status.
- **View Students**: Display a formatted list of all registered students.
- **Search Students**: Find students by their unique ID.
- **Update Students**: Modify student information, including the ability to change IDs.
- **Delete Students**: Remove students from the system by ID.
- **Input Validation**: Comprehensive validation for all inputs to ensure data integrity.
- **Error Handling**: Graceful handling of file operations and invalid data.

## Project Structure
```
Riwi-prueba_desempe-o/
├── README.MD          # Project documentation
├── data/
│   └── students.csv   # Student data storage
└── src/
    ├── main.py        # Main application entry point
    ├── core/
    │   ├── services.py    # Business logic for student operations
    │   └── validators.py  # Input validation functions
    └── utils/
        └── files.py       # CSV file handling utilities
```

## Requirements
- Python 3.10 or higher
- No external dependencies (uses only standard library)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Its-JrDev/Riwi-prueba_desempe-o.git
   cd Riwi-prueba_desempe-o
   ```

2. Ensure Python 3.10+ is installed:
   ```bash
   python --version
   ```

## Usage
1. Navigate to the project directory and run the application:
   ```bash
   python src/main.py
   ```

2. Follow the on-screen menu to perform operations:
   - Select options 1-7 to add, view, search, update, delete students, save data, or exit.
   - The system will guide you through each operation with prompts.

3. Data is automatically loaded from `src/data/students.csv` on startup and saved back when using the save option.

## Data Format
Students are stored with the following fields:
- **ID**: Unique positive integer identifier
- **Name**: Student's full name (string, minimum 2 characters)
- **Age**: Positive integer
- **Course**: One of the available courses (1, 2A, 3, 4B)
- **Status**: 'Active' or 'Not active'

## Future Enhancements
- Add more courses dynamically
- Implement search by name or course
- Add student statistics/reporting
- GUI interface using Tkinter or web interface with Flask
- Database integration (SQLite/PostgreSQL)]

Project Link: [https://github.com/Its-JrDev/Riwi-prueba_desempe-o](https://github.com/Its-JrDev/Riwi-prueba_desempe-o)