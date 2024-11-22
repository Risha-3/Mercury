import csv
import sys
field_names = ["name", "age", "grade"]
data = [ 
    {"name": "Rupert", "age": "20", "grade": "A"}, 
    {"name": "Emma", "age": "21", "grade": "B"}, 
    {"name": "Charlie", "age": "19", "grade": "C"}
]

def add_student(name, age, grade):
    new_student = {"name": name, "age": age, "grade": grade}
    data.append(new_student)
    write_to_csv()

def write_to_csv():
    with open('gradebook.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)  # Correct argument is 'fieldnames'
        writer.writeheader()
        writer.writerows(data)

def main():
    print("""
          Main menu screen
            1.View gradebook
            2.Add student 
            3.Quit program
          """)
    menu_option = int(input("Select option number: "))

    if menu_option == 1:
        result = {}
        with open ('grade_book.csv', mode = 'w') as file:
            csvwriter = csv.writer(file)
            for row in result.items():
                csvwriter.writerow(row)

    if menu_option == 2:
        name_input = input("Enter name: ").strip()
        age_input = input("Enter age: ")
        grade_input = input("Enter grade: ").upper()
        add_student(name_input, age_input, grade_input)

    if menu_option == 3:
        sys.quit()
    
main()
