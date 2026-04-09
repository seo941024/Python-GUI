import random

trials = 100000  # 출력 10개
max_pet = 3
single_prob = 0.03
nx_sequence = [5, 11, 44]

results = []

for t in range(trials):
    pets = 0
    for draws in nx_sequence:
        for _ in range(draws):
            if pets < max_pet and random.random() < single_prob:
                pets += 1
    results.append(pets)

print("10번 시뮬레이션에서 뽑힌 자석펫 수:", results)