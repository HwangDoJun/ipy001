coffee = 3
while 1:
    money = int(input('돈 주세요: '))
    if money == 300:
        coffee -= 1
        print(f'커피 드릴게요. 남은 커피 개수:{coffee}')
    elif money > 300:
        coffee -= 1
        print('거스름돈 %d랑 커피 드릴게요.' % (money - 300))
    else:
        print("돈이나 먹고 떨어져.")
        print("남은 커피는 %d개임")
    if coffee == 0:
        print("커피 없음 ㅅㄱ")
        break