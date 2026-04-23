from bowling_func import BowlingGame
import flet as ft

def main(page: ft.Page):
    page.title = "🎳 Bowling Score Board"
    page.padding = 20

    game = BowlingGame()  # 외부 클래스 있다고 가정
    game_over = False

    frame_container = ft.Container()
    score_container = ft.Container()
    result_text = ft.Text(size=16, weight="bold")

    input_box = ft.TextField(
        label="핀 개수 입력 🎳",
        width=200,
    )

    roll_btn = ft.ElevatedButton("🎯 투구")

    # ================= 프레임 UI =================
    def build_frame_ui(frames):
        return ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        f"{i+1}\n{f}",
                        text_align="center",
                        weight=ft.FontWeight.BOLD,
                        size=30
                    ),
                    width=160 if i == 9 else 100,   # ⭐ 10프레임만 크게
                    height=100,
                    border=ft.border.all(5, "#aa2626"),
                    bgcolor="#FFE4E4",
                    alignment=ft.Alignment(0, 0),
                    border_radius=8,
                )
                for i, f in enumerate(frames)
            ],
            scroll=ft.ScrollMode.AUTO
        )

    # ================= 점수 UI =================
    def build_score_ui(scores):
        return ft.Container(
            content=ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        str(s),
                        weight=ft.FontWeight.BOLD,
                        size=30
                    ),
                    width=160 if i == 9 else 100,   # ⭐ 10프레임만 길게
                    height=100,
                    border=ft.border.all(5, "#2453aa"),
                    bgcolor="#ECEEFF",
                    border_radius=8,
                    alignment=ft.Alignment(0, 0),
                    shadow=ft.BoxShadow(
                            blur_radius=10,
                            color="#00000010"
                        )

                )
                for i, s in enumerate(scores)   # ⭐ 여기 중요
            ],
            scroll=ft.ScrollMode.AUTO
        )
        )
    # ================= 투구 =================
    def roll(e):
        nonlocal game_over

        if game_over:
            return
        
        value = input_box.value

        if not value or not value.isdigit():
            return

        pins = int(value)

        game.add_throw(pins)

        frames = game.show_display()
        scores = game.calculate_live_scores()

        frame_container.content = build_frame_ui(frames)
        score_container.content = build_score_ui(scores)

        input_box.value = ""

        if len(scores) >= 10:
            game_over = True
            input_box.disabled = True
            roll_btn.disabled = True
            result_text.value = f"🎉 게임 종료! 최종 점수: {scores[-1]}"

        page.update()

    roll_btn.on_click = roll

    # ================= UI =================
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "🎳 Bowling Game",
                        size=34,
                        weight=ft.FontWeight.BOLD,
                        color="#1E1E1E"
                    ),
                    alignment=ft.Alignment(0, 0),
                    padding=10
                ),

                ft.Container(
                    content=ft.Row(
                        [input_box, roll_btn],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                    shadow=ft.BoxShadow(
                        blur_radius=15,
                        color="#0000001A"
                    )
                ),

                ft.Divider(),

                ft.Text("🔢 프레임 🔢", size=22, weight=ft.FontWeight.BOLD),
                frame_container,

                ft.Container(height=10),

                ft.Text("🏆 점수 🏆", size=22, weight=ft.FontWeight.BOLD),
                score_container,

                ft.Container(height=10),

                result_text,
            ],
            spacing=10
        )
    )


ft.app(target=main)