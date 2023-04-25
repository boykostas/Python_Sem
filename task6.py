# Решение №1:
# string = input("Введите слово или число: ")
# if (string == string[::-1]):
#     print("Это полиндром!")
# else:
#     print("Это не полиндром")

# Решение №2 рекурсией:
# a = input("Введите слово: ")
# def polindrome(x):
#     if len(x) <=1:
#         return True
#     elif x[0] == x[-1]:
#         return polindrome(x[1:-1])
#     return False
# print(polindrome(a))

