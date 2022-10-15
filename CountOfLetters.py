words = ['aaa', 'bbb', 'ccc', 'aaa', 'bbb', 'ccc', 'aaa', 'bbb', 'ccc']
sumLetters=0

for x in words:
    sumLetters += len(x)

print('Count of letters:', sumLetters)