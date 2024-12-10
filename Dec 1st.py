#STEPS:
# Part 1
# 1. Read file
# 2. Split file into left and right column
# 3. Soft the columns smallest to largest
# 4. Calc. distance and find sum

# Part 2
# 5. Count repeats of left column numebrs in right column and multiply value by repeat times.
# 6. Print results for distance and similarity

# Step 1, open and read input
with open('dec1input.txt', 'r') as file:
    content = file.read()

# Step 2, split the contents into lines and seperate left and right column
lines = content.splitlines()
left_column = []
right_column = [] 

# Parse the file and split each line into two values
for line in lines:
    left, right = map(int, line.split()) # Converts the values to integers
    left_column.append(left)
    right_column.append(right)

# Step 3, sort the columns
left_column.sort()
right_column.sort()

# Step 4, calculate the difference between the pairs in the columns and sum them up
total_distance = 0

for left_val, right_val in zip(left_column, right_column):
    total_distance += abs(left_val - right_val)

# Step 5, for each unique value in the left column, count how many times they repeat in the right column, then multiply the value of the number with its repeat times and add to similarity score
similarity_score = 0

for left_val in set(left_column): # Using set makes sure no duplicates are counted in left column
    repeat_times = right_column.count(left_val)
    similarity_score += left_val * repeat_times

print(f"Total sum of distance: {total_distance}")
print(f"Similarity score: {similarity_score}")