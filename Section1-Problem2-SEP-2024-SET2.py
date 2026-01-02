def within_and_has_double_quotes(s: str) -> bool:
    '''Check if the string is enclosed with double quotes and has double quotes inside.

    Args:
        s : str - input string

    Returns:
        bool - True if the string starts and ends with double quotes and has double quotes inside
    '''
    
    return s[0] == s[-1] == '"' and '"' in s[1:-1]

#Another Method:
# a,b,c=0,0,0
#     if s.startswith("\""):
#         a=1
#     if s.endswith("\""):
#         b=1
#     m=s.strip("\"")
#     if "\"" in m:
#         c=1
        
#     if a+b+c==3:
#         return True
#     else:
#         return False

# Write a function within_and_has_double_quotes that checks if a given string starts and ends with double quotes, and if there are double quotes inside the string (excluding the first and last characters). Return True if both conditions are met, and False otherwise.

# Example cases:

#     • "abcd"efgh" --> True (starts and ends with double quotes, and has double quotes inside)

#     • 'abcd"efgh"' --> False (does not start with double quotes)

#     • "'abcd'efgh'" --> False (uses single quotes)

#     • "abcdefgh" --> False (no double quotes inside the quotes)
