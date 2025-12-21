def student_portal():
    def view_grades():
        print("Your Grades: Math: A, Science: B+, English: A-")
    
    def update_profile():
        print("Updating profile...")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        print(f"Profile updated for {name}")
    
    def enroll_course():
        print("Available courses: Python, Web Dev, Data Science")
        course = input("Enter course to enroll: ")
        print(f"Successfully enrolled in {course}")
    
    def view_schedule():
        print("Your Schedule:\nMonday: Math 10AM\nWednesday: Science 2PM")
    
    def logout():
        print("Logging out...")
        return False
    
    # Switch case using dictionary
    menu = {
        '1': ('View Grades', view_grades),
        '2': ('Update Profile', update_profile),
        '3': ('Enroll Course', enroll_course),
        '4': ('View Schedule', view_schedule),
        '5': ('Logout', logout)
    }
    
    is_logged_in = True
    while is_logged_in:
        print("\n--- Student Portal ---")
        for key, (option, _) in menu.items():
            print(f"{key}. {option}")
        
        choice = input("Enter your choice: ")
        
        if choice in menu:
            _, func = menu[choice]
            if func == logout:
                is_logged_in = func()
            else:
                func()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    student_portal()