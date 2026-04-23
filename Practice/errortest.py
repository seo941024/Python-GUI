import flet as ft

def main(page: ft.Page):
    def click(e):
        print("버튼 눌림🔥")
        page.add(ft.Text("추가됨"))

    btn = ft.ElevatedButton("눌러", on_click=click)

    page.add(btn)

ft.app(target=main)