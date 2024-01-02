import random

# 1~50
# 使用者猜5次
# 猜對提前離開
# 猜錯提示答案
# 提示區間變動

# 題目

start = 1
end = 100

x = random.randint(start, end)
print(f"範圍:{start}~{end}")
# print(x)
# z=10
# 測試分支功能

for i in range(5):
    y = int(input(f"請猜數字({start}~{end}):"))
    if y == x:
        print("猜對了")
        break
    else:
        if y > x:
            if end > y:
                end = y - 1
            print("猜低一點")
        else:
            if start < y:
                start = y + 1
            print("猜高一點")
if y != x:
    print(f"猜錯了，答案是{x}")
else:
    print(f"恭喜過關，共猜了{i+1}次")
