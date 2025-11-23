from datetime import datetime, timedelta

def display_current_datetime():
    global current_date 
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %I:%M:%S")


def calculate_future_date():
    number_of_days = int(input("Enter number of days: "))
    future_date = current_date + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")


print(display_current_datetime())
print(calculate_future_date())