add = input("파일의 이름을 써주세요(파일은 sample폴더안에 들어 있어야 합니다.) : ")
print("add")
add = "./sample/"+add
print("add")
marc = open(add,'rt', encoding='UTF-8')
data=marc.read()
print(data)
#==============================================================
text=data

reader = text[0:24]
print(reader)
finddir = text.index("")

dir = text[24:int(finddir)]

print(dir)

length=12
print([''.join(x) for x in zip(*[list(dir[z::length]) for z in range(length)])]) #디렉토리 부분 12자리씩 끊어 리스트로 저장
#===============================================================
