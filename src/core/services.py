def add_student(students_dict, uid, name, age, course, status):
    """Adds a new student to the dict."""
    students_dict[uid] = {'ID': uid, 'Name': name, 'Age': age, 'Course': course, 'Status': status}
    return students_dict
    
def show_students_list(students_dict):
    """Displays the list of students."""
    print('\n' + '-' * 35); print('      List of Students'); print('-' * 35)
    for i, student_info in enumerate(students_dict.values(), start=1):
        print(f"{i}. ID: {student_info['ID']} | Name: {student_info['Name']} | Age: {student_info['Age']} | Course: {student_info['Course']} | Status: {student_info['Status']} ")
    print('-' * 35)
            
def search_student(students_dict, search_id):
    """Searches for a student by ID."""
    return students_dict.get(search_id)

def update_student_info(students_dict, search_id, new_id, new_name, new_age, new_course, new_status):
    """Updates student info."""
    student = students_dict.get(search_id)
    if not student: return False
    if new_id and new_id != search_id:
        if new_id in students_dict: return False
        del students_dict[search_id]; student['ID'] = new_id; students_dict[new_id] = student
    if new_name: student['Name'] = new_name
    if new_age: student['Age'] = new_age
    if new_course: student['Course'] = new_course
    if new_status: student['Status'] = new_status
    return True

def delete_student(students_dict, search_id):
    """Deletes a student by ID."""
    if search_id in students_dict: del students_dict[search_id]; return True, students_dict
    return False, students_dict
