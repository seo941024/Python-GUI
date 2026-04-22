#time module test

import random
import time

class BowlingGame:
    def __init__(self):
        self.throw_list = []

    def calculate_live_scores(self):
        scores = []
        total = 0
        i = 0

        for _ in range(10):
            if i >= len(self.throw_list):
                break

            if self.throw_list[i] == 10:
                if i + 2 >= len(self.throw_list):
                    break
                total += 10 + self.throw_list[i+1] + self.throw_list[i+2]
                scores.append(total)
                i += 1

            else:
                if i + 1 >= len(self.throw_list):
                    break

                if self.throw_list[i] + self.throw_list[i+1] == 10:
                    if i + 2 >= len(self.throw_list):
                        break
                    total += 10 + self.throw_list[i+2]
                else:
                    total += self.throw_list[i] + self.throw_list[i+1]

                scores.append(total)
                i += 2

        return scores

    def show_display(self):
        display_score = []
        i = 0

        for frame in range(10):
            if i >= len(self.throw_list):
                display_score.append(" ")
                continue

            if frame == 9:
                result = []

                while i < len(self.throw_list):
                    if self.throw_list[i] == 10:
                        result.append("❌")
                        i += 1
                    else:
                        if i+1 < len(self.throw_list):
                            first = self.throw_list[i]
                            second = self.throw_list[i+1]

                            if first + second == 10:
                                result.append(str(first))
                                result.append("/")
                            else:
                                result.append(str(first))
                                result.append(str(second))

                            i += 2
                        else:
                            result.append(str(self.throw_list[i]))
                            i += 1

                display_score.append(" ".join(result))

            else:
                if self.throw_list[i] == 10:
                    display_score.append("❌")
                    i += 1
                else:
                    if i+1 < len(self.throw_list) and self.throw_list[i] + self.throw_list[i+1] == 10:
                        display_score.append(f"{self.throw_list[i]} /")
                    elif i+1 < len(self.throw_list):
                        display_score.append(f"{self.throw_list[i]} {self.throw_list[i+1]}")
                    else:
                        display_score.append(str(self.throw_list[i]))
                    i += 2

        return display_score

    def print_live_board(self):
        frames = self.show_display()
        scores = self.calculate_live_scores()

        print("\n=======================================================")
        print("프레임:", " | ".join(frames))

        score_line = []
        for i in range(10):
            if i < len(scores):
                score_line.append(f"{scores[i]:3}")
            else:
                score_line.append("   ")

        print("점수  :", " | ".join(score_line))
        print("=========================================================\n")

    def add_throw(self, pins):
        self.throw_list.append(pins)
        self.print_live_board()

game = BowlingGame()

# 9프레임 자동 진행
for i in range(9):
    first = random.randint(0, 10)
    time.sleep(1.5)
    game.add_throw(first)

    if first != 10:
        second = random.randint(0, 10 - first)
        time.sleep(1.5)
        game.add_throw(second)

# 10프레임
first = random.randint(0, 10)
time.sleep(1.5)
game.add_throw(first)

if first == 10:
    second = random.randint(0, 10)
else:
    second = random.randint(0, 10 - first)

time.sleep(1.5)
game.add_throw(second)

if first == 10 or first + second == 10:
    third = random.randint(0, 10)
    time.sleep(1.5)
    game.add_throw(third)

# 최종 점수
final_scores = game.calculate_live_scores()
print(f"최종 점수 : {final_scores[-1]}점")