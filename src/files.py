import csv
from pathlib import Path

file_path = Path('./src/data/students.csv')

def save_csv(students_list, include_header=True):
    '''
    Saves the list of students to a CSV file using Path.
    '''
    if not students_list:
        print('\nError: The list of students is empty. Nothing to save.')
        return

    try:
        # 2. Write data to CSV
        with file_path.open(mode='w', newline='', encoding='utf-8') as file:
            
            fieldnames = ['ID', 'Name', 'Age', 'Course', 'Status']

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if include_header:
                writer.writeheader()

            writer.writerows(students_list)
            
        print(f'\nSuccess: List of students saved at: {file_path}')

    except PermissionError:
        print(f'\nError: Permission denied. Close {file_path} and try again.')
    except Exception as e:
        print(f'\nError: An unexpected error occurred: {e}')

def load_csv():
    '''
    Reads a CSV file using Path and returns a list of valid students.
    Skips invalid rows and tracks error count.
    '''
    imported_students = []
    error_count = 0

    # 1. Check if the file exists before opening
    if not file_path.exists():
        print(f'\nError: The file {file_path} was not found.')
        return None, 1

    try:
        with file_path.open(mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    # 2. Extract and clean data
                    # Note: Each row must have exactly the expected columns
                    uid = int(row['ID'])
                    name = row['Name'].strip()
                    age = int(row['Age'])
                    course = row['Course'].strip()
                    status = row['Status'].strip()

                    # 3. Validate non-negative numbers and content
                    if uid < 0 or age < 0 or not name or not uid or not course or not status:
                        error_count += 1
                        continue

                    imported_students.append({
                        'ID': uid,
                        'Name': name,
                        'Age': age,
                        'Course': course,
                        'Status': status
                    })

                except (ValueError, KeyError):
                    # Tracks rows with missing columns or wrong data types
                    error_count += 1
                    continue

        return imported_students, error_count

    except UnicodeDecodeError:
        print('\nError: Encoding issue. The file must be UTF-8.')
        error_count += 1
    except Exception as e:
        print(f'\nError: An unexpected error occurred: {e}')
        error_count += 1
    
    return None, error_count
