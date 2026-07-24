# 영어타자 프로그램

# word.txt 읽어서
# 섞는다 random.suffle
# 임의로 하나 추출 random.choice()

# Q1) then
# input() 결과에 따라 정답!! or 오타!!

# start = time.time()
# 문제 5문제 출제
# 정답 개수
# end = time.time()
# 게임시간 출력
# 출력문 => 게임시간 : 10초, 정답개수 : 3개
# 3개이상 정답인 경우 합격 or 불합격


import random
import time

words = []

with open(f"c:/source/pythonsource/ch1/data/word.txt","r",encoding="utf-8") as f:
    for word in f:
        words.append(word.strip())

start = time.time()
# n : 반복횟수 카운트, corr_cnt : 정답 개수 카운트
n, corr_cnt = 1,0

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print(f"Q{n}")
    print(q)
    answer = input()
    if answer.strip() == q.strip():
        print("정답!!")
        corr_cnt += 1
    else:
        print("오타!!")

    # 문제 개수 추가
    n +=1

end = time.time()

et = end - start
et = format(et, ".3f")

print(f"게임시간 :{et}초, 정답개수 : {corr_cnt}개")

if corr_cnt >= 3:
    print("합격")
else:
    print("불합격")
    
