import streamlit as st
import pandas as pd

# 1. 설정 (반드시 코드 최상단에 위치)
st.set_page_config(page_title="자판기 앱", layout="wide")

# 2. 데이터 초기화
if 'money' not in st.session_state:
    st.session_state.money = 0
if 'inventory' not in st.session_state:
    st.session_state.inventory = {
        "콜라": {"price": 1500, "stock": 10, "emoji": "🥤"},
        "사이다": {"price": 1200, "stock": 8, "emoji": "🫧"},
        "생수": {"price": 800, "stock": 15, "emoji": "💧"},
    }

# 3. 화면 구성
st.title("🥤 스마트 자판기")
st.info(f"### 💰 잔액: {st.session_state.money:,}원")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🛍️ 상품 목록")
    items = st.columns(3)
    for i, (name, info) in enumerate(st.session_state.inventory.items()):
        with items[i]:
            st.write(f"### {info['emoji']} {name}")
            st.write(f"{info['price']}원")
            if st.button(f"{name} 구매", key=name):
                if st.session_state.money >= info['price'] and info['stock'] > 0:
                    st.session_state.money -= info['price']
                    st.session_state.inventory[name]['stock'] -= 1
                    st.success("구매 완료!")
                else:
                    st.error("잔액 부족 또는 품절")

with col2:
    st.subheader("🪙 금액 투입")
    if st.button("＋ 1,000원"):
        st.session_state.money += 1000
        st.rerun()
    if st.button("＋ 500원"):
        st.session_state.money += 500
        st.rerun()
    if st.button("💸 잔돈 반환"):
        st.session_state.money = 0
        st.rerun()

    st.divider()
    st.subheader("📊 재고 현황")
    st.table(pd.DataFrame(st.session_state.inventory).T[['price', 'stock']])