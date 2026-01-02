def walk_L(M):
    path = []
    m = len(M)
    for i in range(m):
        path.append(M[i][0])
    for i in range(1, m):
        path.append(M[m-1][i])
    return path

def walk_Z(M):
    path = []
    m = len(M)
    for i in range(m):
        path.append(M[0][i])
    for i in range(1, m):
        path.append(M[i][m-i-1])
    for i in range(1, m):
        path.append(M[m-1][i])
    return path

def walk_O(M):
    path = []
    m = len(M)
    for i in range(m):
        path.append(M[0][i])
    for i in range(1, m):
        path.append(M[i][m-1])
    for i in range(m-2, -1, -1):
        path.append(M[m-1][i])
    for i in range(m-2, 0, -1):
        path.append(M[i][0])
    return path


def walk_matrix(M, shape):
    """
    Walk along the matrix M according to the specified shape and return the path.

    Args:
        M (list of lists): The square matrix.
        shape (str): Path shape, one of "L", "O", or "Z".

    Returns:
        list: Path along the matrix according to the shape.
    """
    
    
    if shape == 'L':
        return walk_L(M)
    elif shape == 'Z':
        return walk_Z(M)
    elif shape == 'O':
        return walk_O(M)
    else:
        return None

#alternative method
# a=len(M)
#     needlist=[]
#     templist=[]
    
#     if shape == 'L':
#         for i in range(a):
#             needlist.append(M[i][0])
#         for j in range(a):
#             templist.append(M[a-1][j])
#         templist =templist[1:]
#         needlist=needlist+templist
#         return (needlist)
        
        
        
#     if shape == 'Z':
#         for j in range(a):
#             needlist.append(M[0][j])
#         for i in range(a):
#             for j in range(a):
#                 if i+j == a-1 :
#                     templist.append(M[i][j])
#         templist =templist[1:]
#         needlist=needlist+templist
#         templist=[]
        
                
#         for j in range(a):
#              templist.append(M[a-1][j])
             
             
#         templist =templist[1:]
#         needlist=needlist+templist
        
#         return (needlist)
        
#     if shape == 'O':
#         for j in range(a):
#             needlist.append(M[0][j])
#         for i in range(a):
#             templist.append(M[i][a-1])
#         templist =templist[1:]
#         needlist=needlist+templist
#         templist=[]
            
#         for j in range(a-1,-1,-1):
#             templist.append(M[a-1][j])
#         templist =templist[1:]
#         needlist=needlist+templist
#         templist=[]
        
#         for j in range(a-1,-1,-1):
#             templist.append(M[j][0])
#         templist =templist[1:]
#         templist =templist[0:-1:]
        
#         needlist=needlist+templist
        
#         #s=list(set(needlist))
#         return (needlist)

# Matrix Walk
# Given a square matrix, walk along the matrix according to a specified path and return a list of elements based on the path.

# Paths:

#     • "L": Start from the top-left corner and traverse in an "L" shape.

#     • "Z": Start from the top-left corner and traverse the matrix in a "Z" shape.

#     • "O": Start from the top-left corner and traverse the matrix clockwise in an "O" shape.

# Example

# For matrix

# M = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#     • L-shape: [1, 4, 7, 8, 9]

#     • Z-shape: [1, 2, 3, 5, 7, 8, 9]

#     • O-shape: [1, 2, 3, 6, 9, 8, 7, 4]

# Note: "L" has 2 private test cases where "Z" and "O" has one private test case each
            
            
            
    

    
