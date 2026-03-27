#ex04_variable.py 변수/자료형

#여러줄 주석은 여러줄 문자열로 대체 사용
'''
여러줄 문자열을
주석처럼 사용

**자료형**
- 정수(int)
- 실수 (float)
- 문자열(str)
불린(bool)
'''

# val ="'Hello'" #특수문자 /n, /t, /',/" 지원
# val = 10
# val = 3.14
# val = {1,2,3,4}
# val = ...
val = True
print(val)
print(type(val))

age = 20
print('나이는'*age)
print('나이는'+str(age))
print('나이는',age,'입니다')# 여러값을 자동으로 합쳐서 출력하라

#한글로 변수명 지정해도 됨, c/c++동일
이름 = input ('이름>')
나이 = int(input('나이>'))
키 = float(input('키>'))

print('이름:',이름,',나이:',',키:',키)