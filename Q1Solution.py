Here's a Python program to solve the problem:

def calculate_rental_cost(start_time, end_time):
    # Validate input
    if start_time < 0 or end_time < 0 or start_time > 24 or end_time > 24 or start_time >= end_time:
        print("Invalid input")
        return
    
    # Rate definitions
    rates = {
        (0, 7): 500,
        (7, 10): 1000,
        (10, 19): 1500,
        (19, 21): 1000,
        (21, 24): 500,
    }
    
    total_cost = 0
    current_time = start_time
    
    while current_time < end_time:
        for time_range, rate in rates.items():
            if time_range[0] <= current_time < time_range[1]:
                total_cost += rate
                current_time += 1
                break
    
    print(f"Total amount to be paid: RWF {total_cost}")


# Get user input
try:
    start_time = int(input("Enter the starting time (0-24): "))
    end_time = int(input("Enter the ending time (0-24): "))
    calculate_rental_cost(start_time, end_time)
except ValueError:
    print("Invalid input. Please enter integers between 0 and 24.")

How It Works:

1. Input Validation:

Ensures the start and end times are between 0 and 24.

Ensures the start time is less than the end time.



2. Rate Calculation:

Divides the day into time ranges with corresponding rates.

Iterates through the hours rented, adding the appropriate rate for each hour.



3. Output:

Displays the total amount to be paid for the rental.




You can copy and run this code in any Python environment. It prompts for the start and end times and calculates the total rental cost based on the given rates.

