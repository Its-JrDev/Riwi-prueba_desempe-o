import csv
from pathlib import Path

file_path = Path('./data/students.csv')

def save_csv(students_dict, include_header=True):
    '''Saves students dict to CSV.'''
    if not students_dict: print('\nError: The list of students is empty. Nothing to save.'); return
    try:
        with file_path.open(mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Age', 'Course', 'Status'])
            if include_header: writer.writeheader()
            writer.writerows(students_dict.values())
        print(f'\nSuccess: List of students saved at: {file_path}')
    except PermissionError: print(f'\nError: Permission denied. Close {file_path} and try again.')
    except Exception as e: print(f'\nError: An unexpected error occurred: {e}')

def load_csv():
    '''Reads CSV and returns dict of students.'''
    imported_students = {}; error_count = 0
    if not file_path.exists(): print(f'\nError: The file {file_path} was not found.'); return None, 1
    try:
        with file_path.open(mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    uid = int(row['ID']); name = row['Name'].strip(); age = int(row['Age']); course = row['Course'].strip(); status = row['Status'].strip()
                    if uid <= 0 or age <= 0 or not name or not course or not status: error_count += 1; continue
                    imported_students[uid] = {'ID': uid, 'Name': name, 'Age': age, 'Course': course, 'Status': status}
                except (ValueError, KeyError): error_count += 1; continue
        return imported_students, error_count
    except UnicodeDecodeError: print('\nError: Encoding issue. The file must be UTF-8.'); error_count += 1
    except Exception as e: print(f'\nError: An unexpected error occurred: {e}'); error_count += 1
    return None, error_count
