#Python program to check whether the given number is kieth number or not
num = int(input("Enter a number: "))
original_num = num
list1 = []
#To check Number of digits in a Number
while num != 0:
    last_digit = num % 10
    list1.append(last_digit)
    num //= 10
#To Reverse the list  
curr_list = list1[::-1]
list_len = len(curr_list)
print("Length of the current list:", list_len)
#operation to the process of finding kieth number
while curr_list[list_len-1] < original_num:
    next_term = sum(curr_list)
    curr_list.pop(0)
    curr_list.append(next_term)
#Comparing the found number with original number
if curr_list[-1] == original_num:
    print(original_num, "is a Keith number")
else:
    print(original_num, "is not a Keith number")
