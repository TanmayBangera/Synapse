


customers = [[5,2],[5,4],[10,3],[20,1]]

def func(customers):
    current = 0
    total_wait_time = 0
    for arrival, order in customers:
        if(arrival> current):
            current = arrival
        current += order
        total_wait_time += current - arrival
    return total_wait_time/len(customers) 
print(func(customers))       


# Output = 3.25