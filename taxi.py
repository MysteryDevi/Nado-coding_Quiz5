from random import *

operating_time = randint(5, 50)
boarding_customer = 0
for customer in range(1, 51):
    operating_time = randint(5, 50)
    if 5 <= operating_time <= 15:
        print(f"[0] {customer}번째 손님 (소요시간 : {operating_time}분)")
        boarding_customer += 1
    else:
        print(f"[ ] {customer}번째 손님 (소요시간 : {operating_time}분)")
print(f"총 탑승 승객 : {boarding_customer} 분")
