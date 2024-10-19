# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    list1.sort(reverse = True)
    max_ = list1[0]
    for i in list1:
        if i == max_:
            continue
        else:
            print(i)
            break
    
# cách 2:
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     max1 = -float('inf')  
#     max2 = -float('inf')  

#     for i in arr:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif max2 < i < max1:
#             max2 = i
#     print(max2)
