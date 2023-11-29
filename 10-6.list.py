user1_input = input("请输入第一个数字:")
user2_input = input("请输入第二个数字:")
while user1_input != "q" and user2_input != "q":
    try:
        num1 = int(user1_input)
        num2 = int(user2_input)
    except ValueError:
        print("请输入合理的数字.")
        user1_input = input("请输入第一个数字:")
        user2_input = input("请输入第二个数字:")
    else:
        print(num1 + num2)
        user1_input = input("请输入第一个数字:")
        user2_input = input("请输入第二个数字:")


# while True:
#     try:
#         x = input("\nGive me a number: ")
#         if x == 'q':
#             break
#         x = int(x)
#         y = input("Give me another number: ")
#         if y == 'q':
#             break
#         y = int(y)
#     except ValueError:
#         print("Sorry, I really needed a number.")
#     else:
#         sum = x + y
#         print(f"The sum of {x} and {y} is {sum}.")