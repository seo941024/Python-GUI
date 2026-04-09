import random

trials = 100000  # 시뮬레이션 횟수
max_pet = 5      
single_prob = 0.03
nx_sequence = [60]

# 0~5개 카운트 초기화
counts = [0] * (max_pet + 1)

for _ in range(trials):
    pets = 0
    for draws in nx_sequence:
        for _ in range(draws):
            if pets < max_pet and random.random() < single_prob:
                pets += 1
    counts[pets] += 1

# 확률 계산
probabilities = [c / trials * 100 for c in counts]

print("0~5개 합산 횟수:", counts)
print("0~5개 확률(%) :", probabilities)