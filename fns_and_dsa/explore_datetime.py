from datetime import datetime, timedelta

def display_current_datetime():
    global current_date 
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")


def calculate_future_date():
    number_of_days = int(input("Enter number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")


print(f"Current date and time: {display_current_datetime()}")
print(f"Future date: {calculate_future_date()}")