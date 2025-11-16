task = input("Enter your task: ")
time_bound = input("Is it time bound? (yes/no): ")
priority = input("Priority (high, medium, low): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        note = f"'{task}' is a low priority task."


if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
elif time_bound == "no":
    note += " Consider completing it when you have a free time."
    print(f"Note: {note}")
else:
    print("Error")


