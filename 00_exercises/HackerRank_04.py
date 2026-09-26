# The National University conducts an examination of students in subjects.
# Your task is to compute the average scores of each student.


# The format for the general mark sheet is:

# ```
# Student ID → ___1_____2_____3_____4_____5__               
# Subject 1   |  89    90    78    93    80
# Subject 2   |  90    91    85    88    86  
# Subject 3   |  91    92    83    89    90.5
#             |______________________________
# Average        90    91    82    90    85.5 
# ```

# Input Format
# The first line contains and separated by a space.
# The next lines contains the space separated marks obtained by students in a particular subject.

# Output Format
# Print the averages of all students on separate lines.
# The averages must be correct up to decimal place.
# Sample Input

# ```
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5
# ```

# Sample Output

# ```
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5        
# ```

# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(x)]

for student_marks in zip(*marks):
    print(sum(student_marks)/x)
