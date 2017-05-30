"""Test document."""
# mylist = [1,2,3,4,5,6,7,8]
#
# def even_bool(num):
#     return num%2 == 0
#
# evens = filter(even_bool,mylist)
# print(list(evens))


###lambda expression
# evens = filter(lambda  num:num%2 == 0, mylist)
# print(list(evens))

# #str splits
# tweet = "Go Sports! #Sports"
# result = tweet.split('#')[1]
# print(result)

# #in example
# print('x' in [1,2,3,'x'])


# def stringBits(mystring):
#     return mystring[::2]
#
# print(stringBits('whats up'))


# def end_other(a, b):
#     a = a.lower()
#     b = b.lower()
#     # return (b.endswith(a) or a.endswith(b))
#     return a[-len(b):] == b or a == b[-len(a):]
#
# x = end_other('eftg', 'dsfadfdfdfdafdeft')
# print(x)
#
# def doubleChar(mystring):
#     result = ""
#     for i in mystring:
#         result += i*2
#     print(result)
#
# doubleChar('Hi-There')

# def no_teen_sum(a, b, c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)
#
#   # CODE GOES HERE
# def fix_teen(n):
#     if n in [13,14,17,18,19]:
#         return 0
#     return n
#
# print(no_teen_sum(2, 1, 14))
#
# mylist = [1,2,3,4,5,6,7,8]
#
# def even_bool(num):
#     return num%2 == 0
#
# evens = filter(even_bool,mylist)
# print(list(evens))


def count_evens(nums):
    result = 0
    for i in nums:
        if i % 2 == 0:
            result += 1
    return result

print(count_evens([2, 1, 2, 3, 4]))
