import streamlit as st

st.set_page_config(page_title="煮易 CookEasy", page_icon="🍳", layout="wide")
st.title("🍳 煮易 CookEasy")
st.subheader("解決每日煮食煩惱")

# 初始化 session_state
if "family" not in st.session_state:
    st.session_state.family = []

if "dishes" not in st.session_state:
    st.session_state.dishes = []

# ==================== 側邊欄 - 家庭成員 ====================
st.sidebar.header("👨‍👩‍👧‍👦 家庭成員")

with st.sidebar.form("add_family_form", clear_on_submit=True):
    name = st.text_input("成員名稱")
    dislikes = st.text_input("唔鍾意/過敏（用逗號分隔）")
    submitted = st.form_submit_button("新增成員")

    if submitted and name:
        st.session_state.family.append({"name": name, "dislikes": dislikes})
        st.success(f"已新增：{name}")
        st.rerun()

if st.session_state.family:
    st.sidebar.write("目前成員：")
    for member in st.session_state.family:
        st.sidebar.write(f"- {member['name']}")

# ==================== 主畫面 ====================
tab1, tab2 = st.tabs(["📅 今日建議", "📖 我的菜式庫"])

# ==================== Tab 1: 今日建議 ====================
with tab1:
    st.header("📅 今日建議")

    if st.session_state.dishes and st.session_state.family:
        import random
        suggested = random.choice(st.session_state.dishes)

        st.success(f"**今日建議：{suggested['name']}**")
        st.write("**材料：**", ", ".join(suggested['ingredients']))

        if st.button("換另一個建議"):
            st.rerun()
    else:
        st.info("請先喺側邊欄新增家庭成員，同埋喺「我的菜式庫」新增至少一個菜式")

# ==================== Tab 2: 我的菜式庫 ====================
with tab2:
    st.header("📖 我的菜式庫")

    with st.form("add_dish_form", clear_on_submit=True):
        dish_name = st.text_input("菜式名稱")
        ingredients_input = st.text_input("材料（用逗號分隔）")
        dish_submitted = st.form_submit_button("新增菜式")

        if dish_submitted and dish_name and ingredients_input:
            ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]
            st.session_state.dishes.append({
                "name": dish_name,
                "ingredients": ingredients
            })
            st.success(f"已新增菜式：{dish_name}")
            st.rerun()

    if st.session_state.dishes:
        st.write("### 你已儲存嘅菜式：")
        for d in st.session_state.dishes:
            st.write(f"- **{d['name']}**：{', '.join(d['ingredients'])}")
    else:
        st.info("你仲未新增任何菜式")