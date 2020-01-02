a= 'life is too short, you need python'

print(a[3:14])

b='3'

print(a[int(b):int(b)+11]) #문자형을 자료형으로 변환해서 인덱싱

nam = {'name':'namjungduck', 'age':25, 'grade':4} #딕셔너리 자료형으로 변수 nam의 각 성격을 저장해놓음.

print(nam['name']);

print(a[int(nam['grade']-1):int(nam['age']-11)])

print(int(nam['age']-11))
