##pr01_vending.py 자판기 프로그램

menu = ['칠성사이다','펩시콜라','코카콜라','웰치스','백산수']
price = [1900,2100,2200,2000,2300,]

def printmenu():
    print('[자판기 메뉴]')
    for i in range(0,len(menu)):
        print(f'{i+1}. {menu[i]}\t 가격:{price[1]}')
    print()




while True: #while(1) {}
    printmenu()
    sel = int(input ('메뉴번호 선택(종료:0)'))

    if sel ==0:
        break
elif(sel>=1 and sel<len(menu)):
print(f'{menu[sel-1]}선택!')
print('자판기버튼 클릭')