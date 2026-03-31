from files import save_csv, load_csv
from services import add_student, show_students_list, search_student, update_student_info,delete_student
from validators import (
    validate_number, validate_string, validate_uid,
    validate_course, validate_status, validate_ask
    )
    
    
def main():
    
    
    students = []   # In-memory list of dictionaries
    courses =['1', '2A', '3', '4B']
    options = {
        1: 'Add student',
        2: 'Show student\'s list',
        3: 'Search student',
        4: 'Update student log',   # type: ignore
        5: 'Delete student from list',
        6: 'Save students in CSV',
        7: 'Exit'
    }
    
    print('\nInitializing...')
    print('\nImporting data...')
    
    imported_list, errors = load_csv()

    if imported_list is not None:
        students = imported_list
        print(f'\nLoaded data with {errors} errors.\n')
    
    while True:
        print('\n' + '-' * 35)
        print('          Student Manager')
        print('-' * 35)
        for i, opt in options.items():
            print(f'{i}. {opt}')
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
                if not students:
                    print('\nError: List of students is empty.\n')
                else:
                    show_students_list(students)
            case 3:
                if not students:
                    print('\nError: List of students is empty.\n')
                else:
                    search_id = validate_number('Enter ID to search: ', int)
                    student_found = search_student(students, search_id)
                    if student_found:
                        print('\n' + '-' * 35)
                        print('Student Found:')
                        print(f"ID: {student_found['ID']} | Name: {student_found['Name']} | Age: {student_found['Age']} | Course: {student_found['Course']} | Status: {student_found['Status']}")
                        print('-' * 35)
                        
            case 4:
                
                # Update existing student
                
                if not students:
                    print('\nError: List of students is empty.')
                else:
                    search_id = validate_number('Enter ID of student to update their data: ', int)
                    
                    if search_student(students, search_id):
                        new_id = None
                        new_name = None
                        new_age = None
                        new_course = None
                        new_status = None
                        
                        ask = validate_ask('You want to change student\'s ID (S/N)?')
                        if ask == 'S':
                            new_id = validate_number('Enter new value for ID: ', int)
                        ask = validate_ask('You want to change student\'s name (S/N)?')
                        if ask == 'S':
                            new_name = validate_string('Enter new value for name: ')
                        ask = validate_ask('You want to change student\'s age (S/N)?')
                        if ask == 'S':
                            new_age = validate_number('Enter new value for age: ', int)
                        ask = validate_ask('You want to change student\'s course (S/N)?')
                        if ask == 'S':
                            new_course = validate_course('Enter new value for course: ')
                        ask = validate_ask('You want to change student\'s status (S/N)?')
                        if ask == 'S':
                            new_status = validate_status('Enter new value for status: ')
                        
                        

                        update_student_info(students, search_id, new_id, new_name, new_age, new_course, new_status)
                        print('\nStudent updated.')
                    else:
                        print('\nError: Student not found.')
            
            case 5:
                if not students:
                    print('\nError: List of students is empty.')
                else:
                    search_id = validate_number('\nEnter ID to search: ', int)
                    removed, students = delete_student(students, search_id)
                    if removed:
                        print(f'\nStudent with ID: {search_id} removed.')
                    else:
                        print('\nError: Student not found.')
            case 6:
                if not students:
                    print('\nError: List of students is empty.')
                else:
                    save_csv(students)
            case 7:
                print('\nExiting...')
                break
            
            case _: 
                print('\nError: Choose a valid option.')


if __name__ == '__main__':      # Skips indented lines of code if file was imported.
    main()                      # Executes user-defined `def main(): ...` function.