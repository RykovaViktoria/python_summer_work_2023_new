# average = []
# sum = 0
# while True:
#     salary=int(input("Введите зарплату -->"))
#     average.append(n)
#     sum += salary
#     if salary > 0:
#         continue
#     else: break
# print('Средняя зарплата =', sum/len(average))

su = 0
co = 0
while True:
    salary = int(input('--'))
    if salary == 0: break
    su += salary
    co += 1
if co ==0: #Проверить деление на ноль!
    print('sdsff')
else:
    print(su/co)