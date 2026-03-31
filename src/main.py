from utils.files import save_csv, load_csv
from core.services import add_student, show_students_list, search_student, update_student_info, delete_student
from core.validators import validate_number, validate_string, validate_uid, validate_course, validate_status, validate_ask
    
def main():
    """Main function for student management."""
    students = {}; courses = ['1', '2A', '3', '4B']
    options = {1: 'Add student', 2: 'Show student\'s list', 3: 'Search student', 4: 'Update student info', 5: 'Delete student from list', 6: 'Save students in CSV', 7: 'Exit'}
    print('\nInitializing...\nImporting data...')
    imported_list, errors = load_csv()
    if imported_list: students = imported_list; print(f'\nLoaded data with {errors} errors.\n')
    while True:
        print('\n' + '-' * 35); print('          Student Manager'); print('-' * 35)
        for i, opt in options.items(): print(f'{i}. {opt}')
        print('-' * 35)
        select_opt = validate_number('\nSelect an option: ', int)
        match select_opt:
            case 1:
                uid = validate_uid('\nEnter student\'s ID: ', students)
                name = validate_string('Enter student\'s complete name: ')
                age = validate_number('Enter student\'s age: ', int)
                course = validate_course('Enter student\'s course: ', courses)
                status = validate_status('Enter student\'s status: ')
                students = add_student(students, uid, name, age, course, status)
            case 2:
                if not students: print('\nError: List of students is empty.\n')
                else: show_students_list(students)
            case 3:
                if not students: print('\nError: List of students is empty.\n')
                else:
                    search_id = validate_number('Enter ID to search: ', int)
                    student_found = search_student(students, search_id)
                    if student_found:
                        print('\n' + '-' * 35)
                        print('Student Found:')
                        print(f"ID: {student_found['ID']} | Name: {student_found['Name']} | Age: {student_found['Age']} | Course: {student_found['Course']} | Status: {student_found['Status']}")
                        print('-' * 35)
            case 4:
                if not students: print('\nError: List of students is empty.\n')
                else:
                    search_id = validate_number('Enter ID of student to update their data: ', int)
                    if not search_student(students, search_id): print('\nError: Student not found.\n')
                    else:
                        new_id = validate_uid('Enter new value for ID: ', students, search_id) if validate_ask('You want to change student\'s ID (S/N)? ') == 'S' else None
                        new_name = validate_string('Enter new value for name: ') if validate_ask('You want to change student\'s name (S/N)?') == 'S' else None
                        new_age = validate_number('Enter new value for age: ', int) if validate_ask('You want to change student\'s age (S/N)? ') == 'S' else None
                        new_course = validate_course('Enter new value for course: ', courses) if validate_ask('You want to change student\'s course (S/N)? ') == 'S' else None
                        new_status = validate_status('Enter new value for status: ') if validate_ask('You want to change student\'s status (S/N)? ') == 'S' else None
                        print('\nStudent updated successfully.\n' if update_student_info(students, search_id, new_id, new_name, new_age, new_course, new_status) else '\nError: Update failed.\n')
            case 5:
                if not students: print('\nError: List of students is empty.\n')
                else:
                    search_id = validate_number('\nEnter ID to search: ', int)
                    removed, students = delete_student(students, search_id)
                    print(f'\nStudent with ID: {search_id} removed successfully.\n' if removed else '\nError: Student not found.\n')
            case 6:
                if not students: print('\nError: List of students is empty.\n')
                else: save_csv(students)
            case 7: break

if __name__ == '__main__': main()