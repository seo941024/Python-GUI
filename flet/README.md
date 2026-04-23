# 🎳 Bowling Score Board (Python + Flet)

## 📌 프로젝트 소개

이 프로젝트는 Python과 Flet을 활용하여 구현한 **볼링 점수판 GUI 프로그램**입니다.
사용자의 투구 결과를 입력받아 **실시간으로 프레임 점수와 누적 점수**를 시각적으로 표시합니다.

---

## 🚀 주요 기능

* 🎯 투구 입력 (핀 개수 입력)
* 📊 실시간 점수 계산 및 누적 점수 표시
* 🎳 스트라이크 / 스페어 자동 판별
* 🧾 프레임별 점수 시각화
* 🏁 게임 종료 시 최종 점수 출력

---

## 🛠️ 사용 기술

* **Python 3**
* **Flet (GUI Framework)**
* 객체지향 프로그래밍 (OOP)

---

## 📂 프로젝트 구조

```id="p1"
📦 Bowling-Score-Board
 ┣ 📜 main.py              # Flet UI 및 이벤트 처리
 ┣ 📜 bowling_func.py      # 볼링 점수 계산 로직 (BowlingGame 클래스)
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

---

## 🧠 핵심 로직 설명

### 🎳 BowlingGame 클래스

* `throw_list`를 기반으로 투구 기록 저장
* 스트라이크 / 스페어 규칙에 맞게 점수 계산
* 프레임별 누적 점수 반환

### 📊 실시간 점수 처리

* 투구 시마다 `add_throw()` 실행
* UI 즉시 업데이트
* `calculate_live_scores()`로 누적 점수 반영

---

## ▶️ 실행 방법

### 1️⃣ 패키지 설치

```id="p2"
pip install flet
```

### 2️⃣ 실행

```id="p3"
python main.py
```

---

## 💡 실행 화면

* 프레임별 점수 박스 UI
* 점수 누적 표시
* 입력창 + 투구 버튼

---

## 📖 학습 포인트

* 이벤트 기반 GUI 프로그래밍
* 클래스 기반 로직 분리 (UI vs Logic)
* 리스트 및 조건문을 활용한 상태 관리
* 실시간 데이터 업데이트 처리

---

## ✨ 향후 개선 사항

* 🎨 UI 애니메이션 (스트라이크 효과 등)
* 🎮 자동 랜덤 투구 모드 추가
* 📈 점수 그래프 시각화
* 💾 게임 기록 저장 기능

---

## 👤 작성자

* 이름: (지수)
* GitHub: https://github.com/seo941024-cell

---
