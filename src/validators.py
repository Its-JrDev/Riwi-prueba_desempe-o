def validate_number(prompt, data_type):
    while True:
        entry = input(prompt).strip() 
        
        if not entry:
            print('\nError: Field cannot be empty.\n')
            continue
            
        try:
            answer = data_type(entry)
            if answer > 0:
                return answer
            print('\nError: The number must be positive.\n')
        except ValueError:
            type_name = "whole number" if data_type == int else "decimal number"
            print(f'\nError: Please type a valid {type_name}')
            
def validate_string(prompt, min_length=2):
    """
    Asks for a string and ensures it's not empty, 
    meets a minimum length, and isn't just numbers.
    """
    while True:
        entry = input(prompt).strip()
        
        # 1. Check if empty
        if not entry:
            print("\nError: Field cannot be empty.\n")
            continue
        
        # 2. Check minimum length
        if len(entry) < min_length:
            print(f"\nError: Must be at least {min_length} characters long.\n")
            continue
            
        # 3. Check if it's only numbers (Optional, but good for product names)
        if entry.isdigit():
            print("\nError: Name cannot be only numbers.\n")
            continue
            
        return entry

def validate_uid(prompt, students_list):
    """
    Asks for a UID and ensures it is unique within the inventory.
    """
    while True:
        entry = validate_number(prompt, int)
        
        if not entry:
            print("\nError: ID cannot be empty.\n")
            continue
            
        exists = any(student["ID"] == entry for student in students_list)
        
        if exists:
            print(f"\nError: The ID '{entry}' is already registered.\n")
            continue
            
        return entry

def validate_course(prompt, courses):
    while True:
        entry = input(prompt)
        
        if entry not in courses:
            print(f'\nError: Course {entry} doesn\'t exists.\n')
        else: 
            return entry

def validate_status(prompt, status = ['Active', 'Not active']):
    while True:
        entry = validate_string(prompt).lower().capitalize()
        
        if entry not in status:
            print('\nError: Status not valid.\n')
        else:
            return entry
        
def validate_ask(prompt):
    while True:
        answer = input(prompt).capitalize
        if answer not in ['S', 'N']:
            print('\nError: Choose an option between S or N.')
        else:
            return answer