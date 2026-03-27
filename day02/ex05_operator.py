# ex05_operator.py 연산자 학습

a=15
b=14
# 사칙연산
print('덧셈=',a + b)
print('뻴셈=',a - b)
print('곱셈=',a * b)
print('나눗셈=',a / b)
print('몫=',a // b)
print('나머지=',a % b)
print('거듭제곱=',a ** b)

# 할당연산
x=10
print(x)

x += 5 # x = x + 5
print(x)

x-=2
print(x)

x *= 3
print(x)

# 비교연산
print('a==b:',a==b)
print('a!=b:',a!=b)
print('a>b:',a>b)
print('a>=b:',a>=b)
print('a<b:',a<b)
print('a<=b:',a<=b)

#논리연산
age =25
is_license = True

print('나이는 20세 이상이고 면허증 소지'.age>=20 and is_license == True)
print('나이는 20세 이상이고 면허증 소지'.age>=20 and is_license)

print('나이는 20세 이상이거나, 면허증 소지?',age>=20or is_license ==True)

# 맴버연산

fruits = ['사과','바나나','망고','포도']
sentence = '파이썬은 쉬워요!'

print ('과일 중 바나나 존재여부:','바나나' in fruits)
print ('과일 중 수박 존재여부:','수박' in fruits)
print ("문장 내 '파이썬' 단어 여부: ",'파이썬' in sentence)

