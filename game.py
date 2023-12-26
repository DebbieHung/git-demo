import random
#1~50
#使用者猜5次
#猜對提前離開
#猜錯提示答案

#題目
x=random.randint(1,50)
print(x)

for i in range(5):    
    y=int(input('請猜數字(1~50):'))
    if y==x:
        print('猜對了')
        break
    else:
        print('猜錯了')