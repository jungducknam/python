a=1
b=3

while (a<11):
    print("a는",a,"입니다")
    a=a+1

a=0
b=0


a=input("숫자 a 를입력하세요")
print('숫자',a,'를 입력하셨습니다')
b=input("숫자 b 를입력하세요")
print('숫자',b,'를 입력하셨습니다')


def sumab(a,b):
    return a+b

c=sumab(a,b)


print(c)
