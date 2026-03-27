

print('파일 입출력')

#파일쓰기
f= open ('test.txt','w') #쓰기 모드로 파일 오픈
f.write('텍스트를 한줄 씁니다.')
f.write ('텍스트를 두줄 씁니다')

f.close()

# with open('test.txt','w') with 를 사용하면 close() 생략가능