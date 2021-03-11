import random
bingo = [23,45]
min_num = 5
max_num = 50
num = random.randint(min_num,max_num)
if num not in bingo:
  bingo.append(num)
print(bingo)
