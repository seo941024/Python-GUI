import flet as ft
 
def main(page: ft.Page):
    # 1. 페이지 초기 설정
    page.title = "Acoustic AI Intelligence Monitor"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#111418"
    page.padding = 20
   
    # 창 크기 설정
    page.window_width = 1250
    page.window_height = 850
 
    # 2. 공통 카드 스타일 (Flat 디자인)
    def create_card(title, content, expand=False):
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=12, weight=ft.FontWeight.BOLD, color="#5B626A"),
                content
            ], spacing=10),
            bgcolor="#1A1D23",
            padding=15,
            border=ft.border.all(1, "#2D323A"),
            border_radius=0, # 완전 플랫
            expand=expand
        )
 
    # --- 상단 헤더 ---
    header = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN, # 최신 문법 적용
        controls=[
            ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.WAVES, color="#3498DB"),
                    ft.Text("ACOUSTIC AI INTELLIGENCE MONITOR", size=22, weight="bold"),
                ]),
                ft.Text("실시간 음향 패턴 분석 및 이벤트 감지", size=11, color="#5B626A"),
            ], spacing=2),
            ft.Row([
                ft.Container(width=10, height=10, bgcolor="#2ECC71", border_radius=5),
                ft.Text("시스템 정상 운영 중", size=13, color="#2ECC71"),
                ft.Text(" | 2026.10.27 15:45:21", size=13, color="#808B96"),
            ])
        ]
    )
 
    # --- 좌측 섹션 (맵 & 센서) ---
    sensor_map_content = ft.Container(
        bgcolor="black",
        height=250,
        alignment=ft.alignment.center,
        border=ft.border.all(1, "#2D323A"),
        content=ft.Stack([
            ft.Icon(ft.icons.GRID_VIEW, color="#1A1D23", size=200),
            ft.Icon(ft.icons.LOCATION_ON, color="red", left=50, top=50),
            ft.Icon(ft.icons.LOCATION_ON, color="orange", right=60, bottom=70),
        ])
    )
   
    sensor_status_list = ft.Column(spacing=5, scroll=ft.ScrollMode.ADAPTIVE)
    for i in range(1, 13):
        sensor_status_list.controls.append(
            ft.Container(
                content=ft.Row([
                    ft.Text(f"S{i:02d}", size=11, font_family="monospace"),
                    ft.Row([
                        ft.Icon(ft.icons.BATTERY_CHARGING_FULL, size=14, color="#2ECC71"),
                        ft.Text("78%", size=11, color="#2ECC71"),
                    ])
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                bgcolor="#232830", padding=ft.padding.all(8)
            )
        )
   
    left_column = ft.Column([
        create_card("SENSOR LOCATION MAP", sensor_map_content),
        create_card("실시간 센서 상태", ft.Container(content=sensor_status_list, height=300))
    ], width=280, spacing=15)
 
    # --- 중앙 섹션 (스펙트로그램 & 제어) ---
    spectrogram_content = ft.Container(
        bgcolor="black",
        expand=True,
        min_height=350,
        content=ft.Stack([
            # 시뮬레이션 파형 박스
            ft.Container(bgcolor="#3498DB", left=40, bottom=0, width=100, height=180, opacity=0.8),
            ft.Container(bgcolor="#E67E22", left=180, bottom=0, width=150, height=120, opacity=0.8),
            ft.Container(bgcolor="#F1C40F", left=380, bottom=0, width=60, height=220, opacity=0.8),
            # 라벨
            ft.Text("EXCAVATION", color="#3498DB", left=40, top=20, size=10, weight="bold"),
            ft.Text("LEAKAGE", color="#E67E22", left=180, top=40, size=10, weight="bold"),
        ])
    )
 
    control_panel = create_card("AI 모델 및 분석 패널",
        ft.Row([
            ft.Column([
                ft.Text("정확도: 96.7%", size=12, color="#2ECC71"),
                ft.Text("주파수 대역: 100Hz - 18kHz", size=11),
                ft.Row([
                    ft.ElevatedButton("수동 분석", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),
                    ft.OutlinedButton("알람 설정", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),
                ], spacing=10)
            ], expand=1),
            ft.VerticalDivider(color="#2D323A"),
            ft.Column([
                ft.Text("감도 조절 (Sensitivity)", size=11, color="#5B626A"),
                ft.Slider(min=0, max=100, value=75, label="Excavation", active_color="#3498DB"),
                ft.Slider(min=0, max=100, value=85, label="Leakage", active_color="#E67E22"),
            ], expand=1)
        ], height=120)
    )
 
    center_column = ft.Column([
        create_card("REAL-TIME ACOUSTIC SPECTROGRAM", spectrogram_content, expand=True),
        control_panel
    ], expand=True, spacing=15)
 
    # --- 우측 섹션 (이벤트 로그) ---
    event_list = ft.Column(spacing=8, scroll=ft.ScrollMode.ADAPTIVE)
    events = [
        ("15:45:10", "굴착 (구역4)", "98%", "#3498DB"),
        ("15:44:55", "누출 (라인B)", "92%", "#E67E22"),
        ("15:43:30", "침입 (게이트)", "89%", "#F1C40F"),
        ("15:40:12", "정상 신호", "100%", "#5B626A"),
    ]
    for t, e, c, clr in events:
        event_list.controls.append(
            ft.Container(
                padding=12,
                border=ft.border.only(left=ft.border.BorderSide(4, clr)),
                bgcolor="#232830",
                content=ft.Row([
                    ft.Column([
                        ft.Text(e, size=13, weight="bold"),
                        ft.Text(t, size=10, color="#808B96"),
                    ], spacing=2),
                    ft.Container(
                        content=ft.Text(c, size=11, weight="bold", color=clr),
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                        border=ft.border.all(1, clr)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        )
   
    right_column = ft.Column([
        create_card("DETECTED EVENTS LIST", ft.Container(content=event_list, expand=True))
    ], width=320, spacing=15)
 
    # --- 전체 페이지 레이아웃 배치 ---
    page.add(
        header,
        ft.Divider(height=30, color="#2D323A"),
        ft.Row([
            left_column,
            center_column,
            right_column,
        ], expand=True, spacing=15)
    )
 
# 앱 실행
if __name__ == "__main__":
    # 시스템 환경에 따라 WEB_BROWSER 뷰가 가장 안정적입니다.
    ft.app(target=main)