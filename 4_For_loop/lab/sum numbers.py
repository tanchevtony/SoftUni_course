"""
Сумиране на числа
------------------
Да се напише програма, която чете n-на брой цели числа, 
въведени от потребителя и ги сумира.
•	От първия ред на входа се въвежда броят числа n.
•	От следващите n реда се въвежда по едно цяло число.
Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им. 
"""
n = int(input())

sum = 0

for i in range(1, n + 1):
    num = int(input())
    sum += num
print(sum)