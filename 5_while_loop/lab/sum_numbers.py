"""
Сума от числа
Напишете програма, която чете цяло число от конзолата и 
на всеки следващ ред цели числа, докато тяхната сума 
стане по-голяма или равна на първоначалното число. След 
приключване на четенето да се отпечата сумата на 
въведените числа.
"""
number = int(input())

total = 0

while total < number:
    num = int(input())
    total += num
print(total)