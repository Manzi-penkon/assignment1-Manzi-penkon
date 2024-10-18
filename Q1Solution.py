def findRent(start, end):
    # Your code goes here 

    if start >= end or start < 0 or end > 24:
        return "Invalid input"
    
    total_amount = 0
    
    for hour in range(start, end):
        if 0 <= hour < 7 or 21 <= hour < 24:
            total_amount += 500
        elif 7 <= hour < 10 or 19 <= hour < 21:
            total_amount += 1000
        else:  
            total_amount += 1500
    
    print(f"Total amount to be paid: RWF {total_amount}")



 #my codes end here
    return 0

start=int(input("Enter start time"))
end=int(input("Enter end time"))
print(findRent(start,end))
