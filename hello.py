#-*- encoding: utf-8 -*-

print("hello");
a=15 #정수
b="18+14"  #문자
c=0.165 #실수
d=4 #정수
print(a);
print(b);

print();

print(a/d) #나누기
print(a**d) #제곱
print(a%d) #나머지
print("divide:", a//d) #나눗셈 후 몫 반환
########################################################
print()
print("="*30)
print("아래부턴 문자열 자료형")
print("Hello") #문자를 지정할땐 따옴표로 감쌈
print('''h
e
l
l
o'''); #따옴표를 세개 이어 붙이면 코드가 그대로 출력됨
# + 이스케이프 코드 공부 요망
head = "jungduck "
body = "is "
tail = "handsome"
print(head+body+tail); #문자열의 덧셈
print(body*2) # 문자열 곱셈
print(len(head)) #len함수는 문자열의 길이를 나타냄. print 함수로 출력했음
##############################################################
print("="*30)
print()

life="Life is too short, You need python";
#텍스트 인덱싱
print(life[3]); #변수 Life의 세번째 자리의 문자 출력
print(life[13]);
print(life[15-2]); #안에서 사칙연산도 가능
print(life[-1]); #변수 life에서 뒤에서 첫번째 문자
print()

#텍스트 슬라이싱
life="Life is too short, You need python";
b = life[0]+life[1]+life[2]+life[3];
print(b); #변수life의 0에서3까지의 문자 합쳐서 출력
print(life[0:4]); #위와 기능은 똑같음 0에서 3까지의 문자 출력 그러나 뒷자리가 4인 이유는 슬라이싱이 문자를 뽑을때 "0<=life<4" 이런 식으로 뽑기때문에 주의해야함
print(life[8:20]); #"8<=life<20"
print(life[5:]); #"5번째서 부터 문자열 끝까지출력"
print()
#예시
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)
print("="*30)
print()
##################################################################
#문자열 포매팅
print("I eat %d apples." %3) #$d의 내용을 %기호 뒤에있는 3이 대입되었다. 문장과 %사이에 쉼표 안쓰도록 주의!
number = 3
print("I eat %d apples." %number) #변수대입가능

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day)) #두개 이상의 변수를 쓸땐 순서대로 괄호안에 쓰면됨
# %d는 정수, %s는 문자열일때 쓰는 포맷 코드 사용!
print("%10s" % "hi"); #%s문자열 출력 전에 10개의 공백을 만들었음.
print("%-10sjane." % 'hi'); #이번엔 반대로
#문자열 포맷 코드 공부!
print( "I eat {0} apples".format(3)) #format 함수 사용
print("I eat {0} apples".format("five"));
