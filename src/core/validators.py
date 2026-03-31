def validate_number(prompt, data_type):
    """Validates positive number input."""
    while True:
        entry = input(prompt).strip()
        if not entry: print('\nError: Field cannot be empty.\n'); continue
        try:
            answer = data_type(entry)
            if answer > 0: return answer
            print('\nError: The number must be positive.\n')
        except ValueError:
            type_name = "whole number" if data_type == int else "decimal number"
            print(f'\nError: Please type a valid {type_name}')
            
def validate_string(prompt, min_length=2):
    """Validates string input."""
    while True:
        entry = input(prompt).strip()
        if not entry: print("\nError: Field cannot be empty.\n"); continue
        if len(entry) < min_length: print(f"\nError: Must be at least {min_length} characters long.\n"); continue
        if entry.isdigit(): print("\nError: Name cannot be only numbers.\n"); continue
        return entry

def validate_uid(prompt, students_dict, exclude_id=None):
    """Validates unique ID."""
    while True:
        entry = validate_number(prompt, int)
        if not entry: print("\nError: ID cannot be empty.\n"); continue
        if entry in students_dict and entry != exclude_id: print(f"\nError: The ID '{entry}' is already registered.\n"); continue
        return entry

def validate_course(prompt, courses):
    """Validates course selection."""
    while True:
        entry = input(prompt)
        if entry not in courses: print(f'\nError: Course {entry} doesn\'t exist.\n')
        else: return entry

def validate_status(prompt, status=['Active', 'Not active']):
    """Validates status selection."""
    while True:
        entry = validate_string(prompt).lower().capitalize()
        if entry not in status: print('\nError: Status not valid.\n')
        else: return entry
        
def validate_ask(prompt):
    """Validates yes/no input."""
    while True:
        answer = input(prompt).upper().strip()
        if answer not in ['S', 'N']: print('\nError: Choose an option between S or N.')
        else: return answer