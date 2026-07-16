# 화면출력
print("안녕하세요")
print("hello")

i = 1
hap = 0
while i <= 100:
    if i % 3 == 0:
        hap = hap + i
    i = i + 1
print(f"1~100 사이의 3의 배수 총합:{hap}")