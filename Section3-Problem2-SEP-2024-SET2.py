
n = int(input())
for i in range(n):
    print(f"{' '*i}\\{' '*(2*(n-i)-1)}/")
print(f"{' '*n}x")
for i in range(n-1,-1,-1):
    print(f"{' '*i}/{' '*(2*(n-i)-1)}\\")

#alternative method:

# n=int(input())

# for i in range(n,0,-1):
#     print((n-i)*' '   + '\\'  + ((i-1)+(1)+(i-1))*' '  + '/')
    
    
# print(n*' '+'x')


# for i in range(0,n,1):
#     print((n-i-1)*' '   + '/'  + ((i)+(1)+(i))*' '  + '\\')
        
        
# #         5=\ (5-1) +1 + (5-1) /
# # 4=' '\(4-1)+1 (4-1) /
# # 3=' ' '\(3-1)+1+(3-1)/


# Print Pattern - X
# Given an integer n (where n >= 0 ), print an "X" shaped pattern with n rows above and below a central character x. The pattern should use backslashes (\) and forward slashes (/) to form the "X" shape, with increasing spaces between them as they approach the center. There should be no spaces to the right of the pattern.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input

#     • A single integer n, representing the number of rows above and below the center of the "X".

# Output

#     • An "X" shaped pattern with n rows above and below a central x character, as described.

# Examples

# Input:

# 0
# Output:

# x
# Input:

# 1
# Output:

# \ /
#  x
# / \
# Input:

# 2
# Output:

# \   /
#  \ /
#   x
#  / \
# /   \
