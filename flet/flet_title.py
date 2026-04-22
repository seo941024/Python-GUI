import flet as ft

def main(page: ft.Page):
    # ================= 기본 설정 =================
    page.title = "Flet UI Template"
    page.window_width = 400
    page.window_height = 700
    page.bgcolor = "#1e1e1e"
    page.padding = 20

    # ================= 입력 =================
    input_box = ft.TextField(
        hint_text="값 입력",
        border_radius=10,
        border_color="white",
        text_size=14
    )

    # ================= 출력 =================
    output_text = ft.Text(
        value="결과 출력 영역",
        size=16,
        color="white"
    )

    # ================= 버튼 이벤트 =================
    def on_click(e):
        output_text.value = f"입력값: {input_box.value}"
        page.update()

    # ================= 버튼 =================
    btn = ft.ElevatedButton(
        text="실행",
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15
        )
    )

    # ================= 박스 UI (카드 느낌) =================
    container = ft.Container(
        content=ft.Column([
            input_box,
            btn,
            output_text
        ], spacing=15),
        padding=20,
        border_radius=15,
        border=ft.border.all(1, "white"),
        bgcolor="#2b2b2b"
    )

    # ================= 페이지 추가 =================
    page.add(
        ft.Column(
            [
                ft.Text("Flet UI 기본 템플릿", size=20, color="white"),
                container
            ]
        )
    )

ft.app(target=main)