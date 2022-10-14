import math

numbers = [121, 25, 12, 13, 17, 27]
evenSumDigits = []
sumDig=0
totalSum=0
for x in numbers:

    for i in str(x):
        sumDig += int(i)

    if sumDig%2==0:
       evenSumDigits.append(x)

    sumDig=0

print('Sum of elements wits even sum of digits:', (sum(evenSumDigits)))