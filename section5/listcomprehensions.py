# mystring = "hello"
# mylist = []
# for letter in mystring:
#     mylist.append(letter)
# print(mylist)  # output: ['h', 'e', 'l', 'l', 'o']

# # list comprehension

# mystring = "hello"
# mylist = [letter for letter in mystring]
# print(mylist)  # output: ['h', 'e', 'l', 'l', 'o']

# mylist = [x for x in 'word']
# print(mylist)  # output: ['w', 'o', 'r', 'd']

# mylist = [num for num in range(0, 11)]
# print(mylist)  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mylist = [num ** 2 for num in range(0, 11)]
# print(mylist)  # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# mylist = [x for x in range(0, 11) if x % 2 == 0]
# print(mylist)  # output: [0, 2, 4, 6, 8, 10]

# celsius = [0, 10, 20, 34.5]
# fahrenheit = [((9/5) * temp + 32) for temp in celsius]
# print(fahrenheit)  # output: [32.0, 50.0, 68.0, 94.1]


# mylist = []
# for x in [2, 4, 6]:
#     for y in [1, 10, 1000]:
#         mylist.append(x * y)
# print(mylist)  # output: [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

# mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
# print(mylist)  # output: [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]


# result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
# print(result)  # output: [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]


# .gitignore file for pycharm project
# .idea/
# *.iml
# *.ipr
# *.iws
# *.jar
# *.log
# *.patch
# *.swp
# *.bak
# *.pyc
# *.pyo
