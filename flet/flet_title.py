import flet as ft

def main(page: ft.Page):

    def on_click(e):
        input_box.value = ""
        page.update()

    input_box = ft.TextField(
        label="입력창",
        on_submit=on_click
    )

    button = ft.Button(
        content=ft.Text("확인"),
        on_click=on_click
    )

    scroll_area = ft.Column(
        controls=[
            ft.Text(f"아이템 {i}") for i in range(4)
        ]
    )

    # 🔥 핵심: 테두리 + 위에 라벨 겹치기
    item_box = ft.Stack(
        controls=[

            # 박스 (테두리)
            ft.Container(
                content=scroll_area,
                border=ft.border.all(1, "gray"),
                padding=20,
                border_radius=10,
                margin=ft.margin.only(top=10)  # 라벨 공간 확보
            ),

            # 라벨 (위에 떠있는 효과)
            ft.Container(
                content=ft.Text(" 아이템 박스 ", size=12, weight="bold"),
                bgcolor="white",
                padding=5,
                left=20,
                top=0
            )
        ]
    )

    page.add(
        input_box,
        button,
        item_box
    )

ft.app(target=main)