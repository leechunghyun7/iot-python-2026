#ex02_array.py 배열 ->리스트(list)

arr =[30,50,10]
print(arr)

arr.append(70) #리스트 마지막 값 추가
print(arr)

print(arr.index(50)) #리스트 중 요소 위치 리턴

arr2=arr.copy()# 리스트 복사
print(arr)

arr2=arr.copy()#특정 위치값을 추가
print(arr)

arr.insert(2,90) # 특정 위치에 값을 추가
print(arr2)

print (arr2.count(10)) #리스트에 값이 몇개 있는지 확인

print(arr.pop())

arr.remove(50) #50을 지운다는 뜻
print (arr) #리무브는 같은 요소가 있으면 하나만 삭제함

arr.extend(arr2)# 리스트 arr에 리스트 arr2를 전부 합치는 것
print(arr)

arr.reverse()
print(arr)

arr.sort() #ASCending 정렬
print(arr)

arr.sort(reverse=True) #DESC 정렬,python True/False
print(arr)

arr.append('Python')
print(arr)

arr.append([6,7,9])
print(arr)

arr.clear() #모든요소 삭제
print(arr)
