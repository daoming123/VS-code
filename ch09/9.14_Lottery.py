"""导入random的类."""

import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = random.sample(lottery_pool, 4)
print(f"你的彩票号码是{winning_ticket}")
print("本期彩票号码是：24bf")
print("只要彩票上有这 4 个数/字母，你就中奖了！")
