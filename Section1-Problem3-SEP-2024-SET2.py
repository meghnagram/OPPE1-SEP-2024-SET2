def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    '''
    Replace the middle element of a tuple with `n` copies of the middle element.

    Args:
        t (tuple): A tuple with an odd number of elements.
        n (int): The number of times the middle element should be repeated.

    Returns:
        tuple: A new tuple with the middle element replaced by `n` copies.
    '''
    
    
    m = len(t) // 2
    return t[:m] + (t[m],) * n + t[m + 1:]

#another method:
# l=list(t)
#     s=[]
#     m=len(l)
#     mid=(m//2)
#     for i in range(len(l)):
#         if i!=mid:
#             s.append(l[i])
#         else:
#             for a in range(n):
#                 s.append(l[mid])
#     return tuple(s) 


# Replace middle with n times middle
# Given a tuple t of odd length, and a positive integer n, replace the middle element with n copies of itself.

# Examples

# For t = (1, 2, 3, 4, 5) and n = 5, the result should be (1, 2, 3, 3, 3, 3, 3, 4, 5).

# For t = (1, 2, 3) and n = 4, the result should be (1, 2, 2, 2, 2, 3).
        
        
