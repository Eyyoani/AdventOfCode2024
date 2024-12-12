#STEPS:
# Part 1
# 1. Read file and seperate lines
# 2. Check for increasing and decreasing integers
# 3. If row is "safe", increment safe counter

# Part 2
# 4. Add method to remove a number in report and re-check
# 5. Add incrementor to count number of new safe reports
# 6. Print safe reports without and with new safe reports

def check_increasing_or_decreasing(numbers):
    # Ensure all differences are within 1 and 3
    def valid_difference(numbers):
        return all(1 <= abs(numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers) - 1))
    
    # Check if the list is strictly increasing
    is_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1))
    
    # Check if the list is strictly decreasing
    is_decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers) - 1))

    return (is_increasing or is_decreasing) and valid_difference(numbers)

def is_safe_with_one_removal(numbers):
    # Check if removing a single level makes the row safe
    for i in range(len(numbers)):

        # Create a new report excluding the i-th number
        modified_row = numbers[:i] + numbers[i+1:]
        if check_increasing_or_decreasing(modified_row):
            return True
        
    return False

def process_input():
    safe_reports = 0
    safe_with_removal_reports = 0
    
    with open('dec2input.txt', 'r') as file:
        # Read each line, split by spaces and convert to integers
        for line in file:
            numbers = list(map(int, line.split()))

            # Use check method to see if row is safe
            if check_increasing_or_decreasing(numbers):
                safe_reports += 1
            elif is_safe_with_one_removal(numbers):
                safe_with_removal_reports += 1
    
    return safe_reports, safe_with_removal_reports


safe_reports, safe_with_removal_reports = process_input()
print(f"Number of safe reports: {safe_reports}")
print(f"Number of safe reports if one level could be removed: {safe_with_removal_reports+safe_reports}")