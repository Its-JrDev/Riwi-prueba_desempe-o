def add_student(students_list,uid, name, age, course, status):
    student = {
        'ID': uid,
        'Name': name,
        'Age': age,
        'Course': course,
        'Status': status
    }
    students_list.append(student)
    return students_list
    
def show_students_list(students_list):
            print('\n' + '-' * 35)
            print('      List of Students')
            print('-' * 35)
            for i, student_info in enumerate(students_list, start=1):
                print(f"{i}. ID: {student_info['ID']} | Name: {student_info['Name']} | Age: {student_info['Age']} | Course: {student_info['Course']} | Status: {student_info['Status']} ")
            print('-' * 35)
            
def search_student(students_list, search_id):
    for student in students_list:
        if student["ID"] == search_id:
            return student
        return None

def update_student_info(students_list, search_id, new_id= None, new_name= None, new_age= None, new_course= None, new_status= None):
    """

    """

    # Reuse search logic to locate the product
    student = search_student(students_list, search_id)

    if student:
        # Update only fields that were explicitly provided
        if new_id is not None:
            student['ID'] = new_id
        
        if new_name is not None:
            student['Name'] = new_name
        
        if new_age is not None:
            student['Age'] = new_age
            
        if new_course is not None:
            student['Course'] = new_course
        
        if new_status is not None:
            student['Status'] = new_status   

        

        return True  # Update successful

    return False  # Product not found

def delete_student(students_list, search_id):
    # 1. Reuse our search function to check if it exists
    student = search_student(students_list, search_id)
    
    if student:
        # 2. Remove the specific dictionary from the list
        students_list.remove(student)
        return True, students_list # Successfully removed
        
    return False, students_list # Product not found
