# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def is_valid(s):
    if not s.isalnum():
        return False
        
    letter_count = 0
    digit_count = 0
    for ch in s:
        if ch.isdigit():
            digit_count += 1
        else:
            letter_count += 1
            
    if letter_count % 2 == 0 and digit_count % 2 != 0:
        return True
    return False
    
def solution(S):
    # write your code in Python 3.6
    longest = -1
    
    for s in S.split(' '):
        if is_valid(s):
            longest = max(longest, len(s))
            
    return longest