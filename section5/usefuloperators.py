# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for num in range(1, 11):
#     # check if the number is even
#     if num % 2 == 0:
#         print(num)
#     else:
#         print(f"Odd number: {num}")
#
# # output: Odd number: 1


# list(range(0, 11, 2))  # output: [0, 2, 4, 6, 8, 10]

# index_count = 0
# for letter in 'abcde':
#     print(f"At index {index_count} the letter is {letter}")
#     index_count += 1

# enumerate function
# word = 'abcde'
# for item in enumerate(word):
#     print(item)
# # output: (0, 'a')
# #         (1, 'b')
# #         (2, 'c')
# #         (3, 'd')
# #         (4, 'e')
#


# mylist1 = [1, 2, 3]
# mylist2 = ['a', 'b', 'c']
#
# for item in zip(mylist1, mylist2):
#     print(item)
# output: (1, 'a')
#         (2, 'b')
#         (3, 'c')


# mylist1 = [1, 2, 3]
# mylist2 = ['a', 'b', 'c']
#
# list(zip(mylist1, mylist2))  # output: [(1, 'a'), (2, 'b'), (3, 'c')]


# 'x' in [1, 2, 3]  # output: False


# 'a' in 'a world'  # output: True

# 'mykey' in {'mykey': 345}  # output: True


# d = {'mykey': 345}
# var = 345 in d.values()  # output: True
# print(var)


# min([1, 2, 3, 4, 5])  # output: 1

# from random import shuffle
#
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(mylist)
# print(mylist)  # output: [5, 4, 1, 9, 6, 3, 2, 7, 10, 8]


# from random import randint
#
# randint(0, 100)  # output: 76

# input('Enter a number: ')
# output: Enter a number: 50

result = int(input('Enter a number: '))
print(result)

