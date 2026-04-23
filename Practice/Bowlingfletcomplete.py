import flet as ft
import random

class BowlingGame:
    def __init__(self):
        self.throw_list = []

    # -------------------------
    # 🎯 유효성 검사 (완벽 보강)
    # -------------------------
    def is_valid_roll(self, pins):
        throws = self.throw_list
        i = 0
        frame = 1

        # 1~9프레임까지 현재 투구가 어디 위치인지 정확히 추적
        while i < len(throws) and frame < 10:
            if throws[i] == 10:  # 스트라이크인 경우
                i += 1
            else:                # 스트라이크가 아닌 경우 (2구 소모)
                if i + 1 < len(throws):
                    i += 2
                else:
                    # 현재 프레임의 첫 번째 투구만 던진 상태라면 여기서 멈춤
                    break
            frame += 1

        # 이제 'frame'은 현재 투구가 속한 프레임 번호, 'i'는 해당 프레임의 시작 인덱스
        current_frame_throws = throws[i:]

        # 1~9프레임 검증
        if frame < 10:
            if len(current_frame_throws) == 0:
                return True # 첫 번째 투구는 0~10 사이면 무조건 통과 (이미 밖에서 체크됨)
            elif len(current_frame_throws) == 1:
                # 첫 투구가 10(X)이 아닌데, 두 번째 투구와의 합이 10을 넘으면 안 됨
                if current_frame_throws[0] < 10 and current_frame_throws[0] + pins > 10:
                    return False
        
        # 10프레임 검증
        else:
            if len(current_frame_throws) == 1:
                first = current_frame_throws[0]
                # 10프레임 첫 투구가 스트라이크가 아닌데 합이 10을 넘으면 오류
                if first < 10 and first + pins > 10:
                    return False
            elif len(current_frame_throws) == 2:
                first = current_frame_throws[0]
                second = current_frame_throws[1]
                # 보너스 기회가 없는 경우 (합이 10 미만)
                if first + second < 10:
                    return False
                # 보너스 투구 시: 두 번째 투구가 스트라이크가 아닐 때만 세 번째 투구 합산 체크
                if first == 10 and second < 10 and second + pins > 10:
                    return False
        
        return True

    # -------------------------
    # 🧠 점수 계산
    # -------------------------
    def calculate_live_scores(self):
        scores = []
        total = 0
        i = 0
        tl = self.throw_list

        for frame in range(10):
            if i >= len(tl): break

            if frame < 9:
                if tl[i] == 10: # 스트라이크
                    if i + 2 < len(tl):
                        total += 10 + tl[i+1] + tl[i+2]
                        scores.append(total)
                        i += 1
                    else: break
                elif i + 1 < len(tl):
                    if tl[i] + tl[i+1] == 10: # 스페어
                        if i + 2 < len(tl):
                            total += 10 + tl[i+2]
                            scores.append(total)
                            i += 2
                        else: break
                    else: # 오픈
                        total += tl[i] + tl[i+1]
                        scores.append(total)
                        i += 2
                else: break
            else: # 10프레임
                if i + 1 < len(tl):
                    if tl[i] + tl[i+1] >= 10:
                        if i + 2 < len(tl):
                            total += tl[i] + tl[i+1] + tl[i+2]
                            scores.append(total)
                            i += 3
                        else: break
                    else:
                        total += tl[i] + tl[i+1]
                        scores.append(total)
                        i += 2
                else: break
        return scores

    def get_display_data(self):
        display_frames = []
        i = 0
        tl = self.throw_list

        for frame in range(10):
            if i >= len(tl):
                display_frames.append([])
                continue
            if frame == 9:
                shots = []
                for val in tl[i:]:
                    if val == 10: shots.append("X")
                    elif len(shots) > 0 and shots[-1].isdigit() and int(shots[-1]) + val == 10:
                        shots.append("/")
                    else: shots.append("-" if val == 0 else str(val))
                display_frames.append(shots)
                break
            else:
                if tl[i] == 10:
                    display_frames.append([" ", "X"])
                    i += 1
                elif i + 1 < len(tl):
                    f, s = tl[i], tl[i+1]
                    s1 = "-" if f == 0 else str(f)
                    s2 = "/" if f + s == 10 else ("-" if s == 0 else str(s))
                    display_frames.append([s1, s2])
                    i += 2
                else:
                    display_frames.append(["-" if tl[i] == 0 else str(tl[i])])
                    i += 1
        return display_frames

    def is_game_over(self):
        return len(self.calculate_live_scores()) == 10

# ==================================================
# 🎨 UI (코드 유지)
# ==================================================
def main(page: ft.Page):
    page.title = "Bowling System"
    page.bgcolor = "#051622"
    page.padding = 40
    page.width = 1200
    page.height = 700

    game = BowlingGame()
    score_grid = ft.Column(spacing=0)
    error_text = ft.Text("", color="red", size=16)
    info_text = ft.Text("", color="lightgreen", size=16)

    def build_grid():
        frames_data = game.get_display_data()
        live_scores = game.calculate_live_scores()
        header_row, shots_row, total_row = ft.Row(spacing=0, alignment="center"), ft.Row(spacing=0, alignment="center"), ft.Row(spacing=0, alignment="center")

        for i in range(10):
            is_10 = (i == 9)
            w = 150 if is_10 else 90
            highlight = "#FF6B00" if i == len(live_scores) else "#1A374D"
            header_row.controls.append(ft.Container(content=ft.Text(str(i+1), color="white", weight="bold", size=18), width=w, height=40, bgcolor=highlight, alignment=ft.Alignment(0, 0), border=ft.border.all(2, "#333333")))
            
            shots = frames_data[i]
            num_s = 3 if is_10 else 2
            shot_inner = ft.Row(spacing=0)
            for s_idx in range(num_s):
                val = shots[s_idx] if s_idx < len(shots) else ""
                shot_inner.controls.append(ft.Container(content=ft.Text(val, color="white", size=24 if val == "X" else 20, weight="bold"), width=w / num_s, height=50, alignment=ft.Alignment(0, 0), border=ft.border.all(1, "#333333"), bgcolor="#0B2447"))
            shots_row.controls.append(ft.Container(content=shot_inner, width=w))

            curr_score = str(live_scores[i]) if i < len(live_scores) else ""
            total_row.controls.append(ft.Container(content=ft.Text(curr_score, color="#FFD700", size=30, weight="bold"), width=w, height=90, alignment=ft.Alignment(0, 0), border=ft.border.all(1, "#333333"), bgcolor="#124559"))

        score_grid.controls = [header_row, shots_row, total_row]
        if live_scores:
            total = live_scores[-1]
            info_text.value = f"총점: {total} | 평균: {round(total / len(live_scores), 2)} | 스트라이크: {game.throw_list.count(10)}"
        else: info_text.value = ""
        page.update()

    input_box = ft.TextField(label="0~10 입력", width=150, text_align="center", bgcolor="white")

    def do_roll(e):
        error_text.value = ""
        if game.is_game_over():
            error_text.value = "게임 끝났어요!"; page.update(); return
        try:
            p = int(input_box.value)
            if not (0 <= p <= 10): raise ValueError
            if not game.is_valid_roll(p):
                error_text.value = "핀 합이 10을 넘어요!"; page.update(); return
            game.throw_list.append(p)
            input_box.value = ""; build_grid()
        except: error_text.value = "숫자 0~10 입력!"; page.update()

    input_box.on_submit = do_roll
    def reset_game(e): game.throw_list.clear(); error_text.value = ""; info_text.value = ""; build_grid()
    def undo_roll(e):
        if game.throw_list: game.throw_list.pop(); build_grid()
    def auto_roll(e):
        if not game.is_game_over():
            for _ in range(50):
                p = random.randint(0, 10)
                if game.is_valid_roll(p):
                    game.throw_list.append(p); build_grid(); break

    page.add(ft.Column([ft.Text("🎳 Bowling Game 🎳", size=40, weight="bold", color="white"), ft.Container(height=10), score_grid, ft.Container(height=20), info_text, error_text, ft.Row([input_box, ft.ElevatedButton("🎯 투구", on_click=do_roll), ft.ElevatedButton("↩ Undo", on_click=undo_roll), ft.ElevatedButton("🎲 Auto", on_click=auto_roll), ft.ElevatedButton("🔄 Reset", on_click=reset_game)], alignment="center")], horizontal_alignment="center", alignment="center"))
    build_grid()

if __name__ == "__main__":
    ft.app(target=main)