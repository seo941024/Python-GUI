import flet as ft


class BowlingGame:
    def __init__(self):
        self.throw_list = []

    def add_throw(self, pins):
        if len(self.throw_list) < 21:
            self.throw_list.append(pins)

    # -------------------------
    # throw_list → frames
    # -------------------------
    def build_frames(self):
        frames = []
        i = 0

        for frame in range(10):
            if i >= len(self.throw_list):
                break

            if frame == 9:
                frames.append(self.throw_list[i:])
                break

            if self.throw_list[i] == 10:
                frames.append([10])
                i += 1
            else:
                if i + 1 < len(self.throw_list):
                    frames.append([self.throw_list[i], self.throw_list[i + 1]])
                else:
                    frames.append([self.throw_list[i]])
                i += 2

        return frames

    # -------------------------
    # 점수 계산
    # -------------------------
    def calc_scores(self, frames):
        scores = []
        total = 0

        flat = [pin for frame in frames for pin in frame]

        i = 0
        for frame in range(len(frames)):
            if i >= len(flat):
                break

            if flat[i] == 10:
                if i + 2 < len(flat):
                    score = 10 + flat[i + 1] + flat[i + 2]
                else:
                    break
                i += 1

            elif i + 1 < len(flat) and flat[i] + flat[i + 1] == 10:
                if i + 2 < len(flat):
                    score = 10 + flat[i + 2]
                else:
                    break
                i += 2

            else:
                if i + 1 < len(flat):
                    score = flat[i] + flat[i + 1]
                else:
                    break
                i += 2

            total += score
            scores.append(total)

        return scores

    # -------------------------
    # 출력 포맷
    # -------------------------
    def format_frames(self, frames):
        result = []

        for i, frame in enumerate(frames):
            temp = []

            if i == 9:
                for j, val in enumerate(frame):
                    if val == 10:
                        temp.append("❌")
                    elif j > 0 and frame[j - 1] != 10 and frame[j - 1] + val == 10:
                        temp.append("/")
                    else:
                        temp.append("-" if val == 0 else str(val))
            else:
                if frame[0] == 10:
                    temp.append("❌")
                else:
                    first = frame[0]
                    second = frame[1] if len(frame) > 1 else None

                    temp.append("-" if first == 0 else str(first))

                    if second is not None:
                        if first + second == 10:
                            temp.append("/")
                        else:
                            temp.append("-" if second == 0 else str(second))

            result.append(" ".join(temp))

        return result


# -------------------------
# Flet UI
# -------------------------

def main(page: ft.Page):
    game = BowlingGame()

    page.title = "🎳 Bowling Game"

    # 🔥 Column을 변수로 잡아야 함 (핵심)
    main_col = ft.Column()

    input_field = ft.TextField(label="핀 개수 (0~10)", width=200)

    def update_ui():
        frames = game.build_frames()
        scores = game.calc_scores(frames)
        display = game.format_frames(frames)

        # 🔥 새 Row 생성
        new_frame_row = ft.Row()
        new_score_row = ft.Row()

        for i in range(10):
            text = display[i] if i < len(display) else "·"

            new_frame_row.controls.append(
                ft.Container(
                    content=ft.Text(text, size=20, weight=ft.FontWeight.BOLD),
                    width=80,
                    height=60,
                    alignment=ft.alignment.center,
                    border=ft.border.all(1),
                    border_radius=10
                )
            )

            score = str(scores[i]) if i < len(scores) else ""

            new_score_row.controls.append(
                ft.Container(
                    content=ft.Text(score, size=16),
                    width=80,
                    height=40,
                    alignment=ft.alignment.center,
                    border=ft.border.all(1),
                    border_radius=10
                )
            )

        # 🔥 Column 전체 교체 (이게 핵심)
        main_col.controls[1] = new_frame_row
        main_col.controls[2] = new_score_row

        page.update()

    def add_click(e):
        try:
            val = int(input_field.value)

            if 0 <= val <= 10:
                game.add_throw(val)
                input_field.value = ""
                update_ui()

        except:
            input_field.value = ""

    add_btn = ft.ElevatedButton("추가", on_click=add_click)

    # 초기 UI 구조 (빈 Row 자리 확보)
    main_col.controls = [
        ft.Text("🎳 볼링 점수판", size=30, weight=ft.FontWeight.BOLD),
        ft.Row(),  # frame 자리
        ft.Row(),  # score 자리
        ft.Row([input_field, add_btn])
    ]

    page.add(main_col)
    update_ui()


ft.app(target=main)