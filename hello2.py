#f문자열 포매팅
name = 'jungduck nam';
age = 25;
a= f"my name is {name}, I'm {age} years old soon";
print(a);
print("="*30)
#================================================================
#문자열 관련 함수들
a = "hobby"
print(a.count('b')); #변수 a중 b의 개수를 카운팅

a = "Python is the best choice"
print(a.find('b')); #해당 문자열이 있는 주소를 숫자로 알려줌. 없으면 -1값을 반환
print(a[a.find('t')]);#해당 숫자를 반대로 인덱싱하기
print(a.index('t')) #index도 find와 기능은 똑같음. 그러나 찾는 문자열이 없을시 오류를 내보낸다.

print(",".join('wa sands!')); #조인은 문자열사이사이에 앞에서 명시한 문자열을 넣어준다

a = "       hello        "
print(a.rstrip()) #문자열의 오른쪽 공백 삭제
print(a.strip())  #양옆 공백 삭제
print(a.lstrip()) #문자열의 왼쪽 공백 삭제

a = "Life is too short";
print(a.replace("Life", "Your leg")); #life를 your leg로 치환

a = "Life is too short"
print(a.split()) #split함수는 기본적으로 띄어쓰기를 기준으로 문자를 나눠준다

b = "a:b:c:d"
print(b.split(':')) #괄호안에 문자를 쓰면 그 문자를 기준으로 나눠준다
print("="*30)
#===========================================================================
#리스트 자료형
#리스트의 유형들
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(b[0]+b[2]) #리스트 b의 0번째 값과 2번째 값을 더함

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][0]) #리스트안의 리스트를 출력하는 방법

print(ord(""))
print(chr(31))
