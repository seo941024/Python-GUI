import flet as ft
import random


def main(page: ft.Page):
    page.title = "Simple Market"
    page.bgcolor = "#fafafa"  # 전체 밝은 회색(눈 편함)

    # -------------------------
    # 데이터
    # -------------------------
    items = [f"상품{i}" for i in range(1, 101)]

    market = {}
    x = 0

    while x < len(items):
        mid = random.randint(1, 100000)

        if mid in market:
            continue

        market[mid] = {
            "name": items[x],
            "stock": random.randint(1, 50),
            "price": random.randint(10, 100) * 100
        }
        x += 1

    # -------------------------
    # 상태
    # -------------------------
    cart = []
    total_cash = 0
    today_total = 0

    # -------------------------
    # UI
    # -------------------------
    name_input = ft.TextField(label="상품 이름", border_color="#fdd835")
    qty_input = ft.TextField(label="수량", border_color="#fdd835")

    output = ft.Text(color="#333")

    total_text = ft.Text("총 금액: 0원", size=16, weight="bold", color="#333")
    today_text = ft.Text("오늘 총 매출: 0원", size=14, weight="bold", color="#333")

    cart_view = ft.Column(scroll=True, height=250)
    danger_view = ft.Column(scroll=True, height=400)
    discount_view = ft.Column(scroll=True, height=400)

    # -------------------------
    # 위험 재고 (톤 다운된 경고색)
    # -------------------------
    def load_danger():
        danger_view.controls.clear()

        for v in market.values():
            if v["stock"] <= 5:
                danger_view.controls.append(
                    ft.Container(
                        content=ft.Text(
                            f"{v['name']} | 재고:{v['stock']}",
                            color="#5d4037"  # 부드러운 갈색 텍스트
                        ),
                        bgcolor="#fff3e0",  # 연한 주황 (부드러운 경고)
                        padding=8,
                        border_radius=10,
                        border=ft.border.all(1, "#ffcc80")
                    )
                )

        page.update()

    # -------------------------
    # 할인
    # -------------------------
    def load_discount():
        discount_view.controls.clear()
        used = set()

        for _ in range(5):
            k = random.choice(list(market.keys()))

            if k in used:
                continue

            used.add(k)
            v = market[k]

            old = v["price"]
            v["price"] = int(old * 0.9)

            discount_view.controls.append(
                ft.Container(
                    content=ft.Text(
                        f"{v['name']}  {old} → {v['price']}",
                        color="#4e342e"
                    ),
                    bgcolor="#fffde7",
                    padding=6,
                    border_radius=8,
                    border=ft.border.all(1, "#ffe082")
                )
            )

    # -------------------------
    # 상품 찾기
    # -------------------------
    def find(name):
        for k, v in market.items():
            if v["name"] == name:
                return k, v
        return None, None

    # -------------------------
    # 장바구니
    # -------------------------
    def add_cart(e):
        nonlocal total_cash

        name = name_input.value.strip()
        qty = qty_input.value

        if not name or not qty or not qty.isdigit():
            output.value = "입력 오류"
            page.update()
            return

        qty = int(qty)

        k, v = find(name)

        if not v:
            output.value = "상품 없음"
            page.update()
            return

        if v["stock"] < qty:
            output.value = "재고 부족 ⚠"
            page.update()
            return

        price = v["price"] * qty
        v["stock"] -= qty

        cart.append((k, v["name"], qty, price))

        cart_view.controls.append(
            ft.Container(
                content=ft.Text(f"{v['name']} x{qty} = {price}원"),
                padding=6,
                bgcolor="#fffde7",
                border_radius=8,
                border=ft.border.all(1, "#ffe082")
            )
        )

        total_cash += price
        total_text.value = f"총 금액: {total_cash}원"

        output.value = "추가 완료"

        name_input.value = ""
        qty_input.value = ""

        load_danger()
        page.update()

    # -------------------------
    # 구매
    # -------------------------
    def buy(e):
        nonlocal total_cash, today_total

        receipt = "=== 영수증 ===\n"

        for k, name, qty, price in cart:
            receipt += f"{name} x{qty} = {price}원\n"

        receipt += f"\n이번 구매: {total_cash}원"

        today_total += total_cash

        receipt += f"\n오늘 총 매출: {today_total}원"

        with open("receipt.txt", "w", encoding="utf-8") as f:
            f.write(receipt)

        cart.clear()
        cart_view.controls.clear()
        total_cash = 0

        total_text.value = "총 금액: 0원"
        today_text.value = f"오늘 총 매출: {today_total}원"

        output.value = "구매 완료"

        page.update()

    # -------------------------
    # UI Layout
    # -------------------------
    page.add(
        ft.Container(
            padding=10,
            content=ft.Row(
                expand=True,
                controls=[

                    # LEFT
                    ft.Container(
                        width=260,
                        bgcolor="white",
                        padding=12,
                        border=ft.border.all(2, "#ffe082"),
                        border_radius=12,
                        content=ft.Column([
                            ft.Text("⚠ 위험 재고", weight="bold", color="#5d4037"),
                            danger_view
                        ])
                    ),

                    # CENTER
                    ft.Container(
                        expand=True,
                        padding=20,
                        bgcolor="white",
                        border=ft.border.all(2, "#ffe082"),
                        border_radius=12,
                        content=ft.Column([

                            ft.Text("🛒 Simple Market", size=22, weight="bold", color="#4e342e"),

                            name_input,
                            qty_input,

                            ft.Row([
                                ft.ElevatedButton("장바구니", on_click=add_cart, bgcolor="#ffe082", color="#4e342e"),
                                ft.ElevatedButton("구매", on_click=buy, bgcolor="#ffd54f", color="#4e342e"),
                            ]),

                            ft.Divider(),

                            ft.Text("🧾 장바구니"),
                            cart_view,

                            ft.Divider(),

                            total_text,
                            today_text,

                            ft.Divider(),

                            output
                        ])
                    ),

                    # RIGHT
                    ft.Container(
                        width=260,
                        bgcolor="white",
                        padding=12,
                        border=ft.border.all(2, "#ffe082"),
                        border_radius=12,
                        content=ft.Column([
                            ft.Text("💛 할인 목록", weight="bold", color="#5d4037"),
                            discount_view
                        ])
                    )
                ]
            )
        )
    )

    load_danger()
    load_discount()


ft.app(target=main)