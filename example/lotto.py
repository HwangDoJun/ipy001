def lotto():
    from random import randint
    lotto=[]
    while (len(lotto)<6):
        pick = randint(1,45)
        if pick not in lotto:lotto.append(pick)
    lotto.sort()
    return lotto
print(lotto())
t.sleep(1)
print('에러체크를 시도하겠습니다.')
def ck():
    for k in range(1000):
        out = lotto()
        ck = len(set(out))
        if ck != 6:
            print(k+1, '번째 중복 발생', out)
            break
        if ck == 0 and (k+1) == 1000:
            print(k+1, '이상없이 체크완료')