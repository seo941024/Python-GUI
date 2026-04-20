import flet as ft
import random


def main(page: ft.Page):
    page.title = "Simple Market"
    page.bgcolor = "#fffde7"

    # -------------------------
    # 데이터
    # -------------------------
    items = [
        "비누", "치약", "샴푸", "린스", "바디워시", "폼클렌징", "칫솔", "수건",
        "휴지", "물티슈", "세탁세제", "섬유유연제", "주방세제", "수세미", "고무장갑",
        "쌀", "라면", "햇반", "생수", "우유", "계란", "두부", "콩나물", "시금치",
        "양파", "감자", "고구마", "사과", "바나나", "오렌지", "귤", "토마토",
        "김치", "된장", "고추장", "간장", "식용유", "참기름", "소금", "설탕",
        "커피", "차", "과자", "빵", "젤리", "초콜릿", "음료수", "맥주", "소주",
        "고기(돼지고기)", "고기(소고기)", "닭고기", "생선", "오징어", "새우", "게",
        "쌀국수", "파스타", "잼", "버터", "치즈", "요거트", "아이스크림", "통조림",
        "냉동만두", "어묵", "햄", "소시지", "김", "미역", "다시마", "멸치",
        "밀가루", "부침가루", "튀김가루", "빵가루", "식초", "소스", "향신료",
        "양초", "성냥", "건전지", "전구", "쓰레기봉투", "지퍼백", "호일", "랩"
    ]

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
    name_input = ft.TextField(label="상품 이름")
    qty_input = ft.TextField(label="수량")

    output = ft.Text(color="black")
    total_text = ft.Text("총 금액: 0원", size=16, weight="bold", color="black")
    today_text = ft.Text("오늘 총 매출: 0원", size=14, weight="bold", color="black")

    cart_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    danger_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    discount_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    # -------------------------
    # 위험 재고
    # -------------------------
    def load_danger():
        danger_view.controls.clear()

        for v in market.values():
            if v["stock"] <= 5:
                danger_view.controls.append(
                    ft.Container(
                        content=ft.Text(
                            f"{v['name']} | 재고:{v['stock']}",
                            color="black"
                        ),
                        padding=8,
                        border_radius=8,
                        bgcolor="white",
                        border=ft.border.all(2, "#ef9a9a")
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
                        color="black"
                    ),
                    padding=8,
                    border_radius=8,
                    bgcolor="white",
                    border=ft.border.all(2, "#ffe082")
                )
            )

        page.update()

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
            output.value = "재고 부족"
            page.update()
            return

        price = v["price"] * qty
        v["stock"] -= qty

        cart.append((k, v["name"], qty, price))

        cart_view.controls.append(
            ft.Container(
                content=ft.Text(
                    f"{v['name']} x{qty} = {price}원",
                    color="black"
                ),
                padding=8,
                border_radius=8,
                bgcolor="white",
                border=ft.border.all(2, "#ffe082")
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

        today_total += total_cash

        receipt += f"\n이번 구매: {total_cash}원"
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
    # UI Layout (괄호 수정 완료)
    # -------------------------
    page.add(
        ft.Row(
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[

                # LEFT
                ft.Container(
                    border=ft.border.all(2, "#eccb5e"),
                    width=250,
                    bgcolor="#f7f3c5",
                    padding=10,
                    border_radius=8,
                    content=ft.Column([
                        ft.Text("⚠ 재고 부족 (5개 이하)", color="black", weight="bold"),
                        danger_view
                    ])
                ),

                # CENTER
                ft.Container(
                    border=ft.border.all(2, "#eccb5e"),
                    expand=True,
                    padding=20,
                    bgcolor="white",
                    border_radius=8,
                    content=ft.Column([

                        ft.Text("🛒 Simple Market", size=22, weight="bold", color="black"),

                        name_input,
                        qty_input,

                        ft.Row([
                            ft.OutlinedButton(
                                "장바구니",
                                on_click=add_cart,
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(2, "#eccb5e"),
                                    color="black"
                                )
                            ),
                            ft.OutlinedButton(
                                "구매",
                                on_click=buy,
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(2, "#eccb5e"),
                                    color="black"
                                )
                            ),
                        ]),

                        ft.Divider(),

                        ft.Text("🧾 장바구니", color="black"),
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
                    border=ft.border.all(2, "#eccb5e"),
                    width=250,
                    bgcolor="#f7f3c5",
                    padding=10,
                    border_radius=8,
                    content=ft.Column([
                        ft.Text("💛 할인 목록", color="black", weight="bold"),
                        discount_view
                    ])
                )
            ]
        )
    )

    load_danger()
    load_discount()


ft.app(target=main)