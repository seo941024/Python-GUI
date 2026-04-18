import random as rd

user_nums = []


while len(user_nums) < 6:
    try:
        n = int(input("번호를 입력하세요 (1~43): "))
        
        if n < 1 or n > 43:
            print("1 ~ 43 사이 숫자만 입력하세요")
        elif n in user_nums:
            print("중복된 숫자입니다.")
        else:
            user_nums.append(n)
            
    except:
        print("숫자만 입력하세요.")


lotto = rd.sample(range(1, 44), 7)


main_lotto = lotto[:6]
bonus = lotto[6]


lotto_sorted = sorted(main_lotto)
user_sorted = sorted(user_nums)

print(f"당첨 번호: {lotto_sorted} + 보너스 [{bonus}]")
print(f"내 번호: {user_sorted}")


match = len(set(user_nums) & set(main_lotto))


bonus_match = bonus in user_nums


if match == 6:
    print("1등!!!")
elif match == 5 and bonus_match:
    print("2등!!")
elif match == 5:
    print("3등!")
elif match == 4:
    print("4등")
elif match == 3:
    print("5등")
else:
    print("꽝")