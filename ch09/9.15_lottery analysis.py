"""彩票中奖几率."""

import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = [1, 'a', 7, 'c']

count = 0

while True:
    count += 1
    winning_ticket = random.sample(lottery_pool, 4)
    if winning_ticket == my_ticket:
        print(f"中奖了！号码是：{winning_ticket}")
        print(f"执行了 {count} 次循环才中！")
        break
