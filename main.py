students = {
    "s01": {"name": "Teston", "group": "Python263", "grades": [12, 12, 12]},
    "s02": {"name": "Kate", "group": "Python263", "grades": []},
    "s03": {"name": "Tom", "group": "CSharp263", "grades": [11]},
    "s04": {"name": "Bob", "group": "CSharp263", "grades": [7, 2]},
    "s05": {"name": "Arthur", "group": "Python263", "grades": []},
    "s06": {"name": "Jane", "group": "CSharp263", "grades": [12, 11, 12]},
    "s07": {"name": "Sam", "group": "Python263", "grades": [9, 8, 9]},
    "s08": {"name": "Todd", "group": "Python263", "grades": [9, 8, 9]},
    "s09": {"name": "Rick", "group": "Python262", "grades": [12, 12, 12, 11, 12]},
    "s10": {"name": "Alice", "group": "CSharp263", "grades": [4, 3, 5]},
}
all_commands = {
    "help": "Show all commands",
    "exit": "Ends programm",
    "st": "Show all student data",
    "st<ID>": "Shows selected students data"
}

while True:
    entered = input("Enter command").split()
    command = entered[0]

    if command == "help":
    #     "help": "Show all commands",
    # "exit": "Ends programm",
    # "st": "Show all student data",
        for key in all_commands.keys():

            print(f"{key} - {all_commands[key]}")
        
        
    elif command =="exit":
        print("Goodbye!")
        break
    elif command == "st":
         print("ID - name - group - grades")
         for st_id in students.keys():
            student = students[st_id]
            grades = student["grades"]
            for i in range(len(grades)):
                grades[i] = str(grades[i])

            if len(grades) == 0:
                grades_str = "Empty grades"
            else:
                grades_str = " ".join(grades)  
                 
            print(f"{st_id} - {student["name"]} - {student["group"]} - {student["grades_str"]} ")

        #<ID> - <name> - <group> - <grades>

    print()
