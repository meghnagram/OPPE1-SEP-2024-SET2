def count_positive_ignore_none(nums: list):
    '''
    Count the number of positive integers in the list, ignoring `None` values and zeros.

    Args:
        nums (list): A list of numbers, possibly containing `None` values.

    Returns:
        int: The count of positive integers in the list.
    '''
    
    
    # 1 - Basic method
    # count =0
    # for num in nums:
    #     if num is not None and num>0:
    #         count += 1
    # return count

    # 2 - Comprehensions
    # return len([num for num in nums if num is not None and num>0])

    # 3 - functional
    return len(list(filter(lambda x : x is not None and x>0, nums)))
    
#another method:
# count=0
    
#     for i in nums:
#         if type(i)==int:
#             if i>0:
#                 count +=1
#     return count

# Count Positive Integers Ignoring None
# Given a list which contains integers and None, count the number of positive integers while ignoring None values. Zero should not be counted.

# Example

# For the list [1, -2, 3, 0, None, 4], the result should be 3 because the positive integers are 1, 3, and 4.

# Explanation

#     • We ignore None values.

#     • We also ignore 0 because it is not positive.

#     • The positive integers are 1, 3, and 4, so the count is 3.
