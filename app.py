import streamlit as st
import random

st.set_page_config(page_title="煮易 CookEasy", page_icon="🍳", layout="wide")
st.title("🍳 煮易 CookEasy")
st.subheader("解決每日煮食煩惱")

# ==================== 內置菜式庫 ====================
DEFAULT_DISHES = [
    {"name": "蒜蓉蒸排骨", "ingredients": ["排骨", "蒜蓉", "生抽", "蠔油"]},
    {"name": "番茄炒蛋", "ingredients": ["番茄", "蛋", "糖", "生抽"]},
    {"name": "豉汁蒸魚", "ingredients": ["魚", "豆豉", "薑", "蔥"]},
    {"name": "涼瓜炒蛋", "ingredients": ["涼瓜", "蛋", "蒜蓉", "生抽"]},
    {"name": "菠菜炒蛋", "ingredients": ["菠菜", "蛋", "蒜蓉"]},
    {"name": "薑蔥蒸蠔", "ingredients": ["蠔", "薑", "蔥", "生抽"]},
    {"name": "柱侯牛腩", "ingredients": ["牛腩", "柱侯醬", "薑", "八角"]},
    {"name": "白切雞", "ingredients": ["雞", "薑", "蔥", "生抽"]},
    {"name": "蠔油生菜", "ingredients": ["生菜", "蠔油", "蒜蓉"]},
    {"name": "肉片炒西蘭花", "ingredients": ["西蘭花", "豬肉", "蒜蓉", "生抽"]},
    {"name": "蛋炒飯", "ingredients": ["飯", "蛋", "蔥", "生抽"]},
    {"name": "椒鹽排骨", "ingredients": ["排骨", "椒鹽粉", "蒜蓉"]},
    {"name": "冬菇燉雞", "ingredients": ["雞", "冬菇", "薑", "紅棗"]},
    {"name": "魚香茄子", "ingredients": ["茄子", "豬肉", "豆瓣醬", "蒜蓉"]},
    {"name": "麻婆豆腐", "ingredients": ["豆腐", "豬肉", "豆瓣醬", "花椒"]},
]

# 初始化 session_state
if "family" not in st.session_state:
    st.session_state.family = []

# ==================== 側邊欄 - 家庭成員 ====================
st.sidebar.header("👨‍👩‍👧‍👦 家庭成員")

with st.sidebar.form("add_family_form", clear_on_submit=True):
    name = st.text_input("成員名稱")
    dislikes = st.text_input("唔鍾意/過敏（用逗號分隔）")
    submitted = st.form_submit_button("新增成員")

    if submitted and name:
        st.session_state.family.append({"name": name, "dislikes": dislikes})
        st.success(f"已新增：{name}")

if st.session_state.family:
    st.sidebar.write("目前成員：")
    for member in st.session_state.family:
        st.sidebar.write(f"- {member['name']}")

# ==================== 主畫面 ====================
tab1, tab2 = st.tabs(["📅 今日建議", "📖 所有菜式"])

# ==================== Tab 1: 今日建議 ====================
with tab1:
    st.header("📅 今日建議")

    # 簡單過濾（如果有家庭成員輸入唔鍾意，可以之後加強）
    available_dishes = DEFAULT_DISHES.copy()

    if st.button("🔄 隨機建議一個菜式", use_container_width=True):
        suggested = random.choice(available_dishes)
        st.session_state.suggested = suggested

    if "suggested" in st.session_state:
        dish = st.session_state.suggested
        st.success(f"**今日建議：{dish['name']}**")
        st.write("**材料：**", ", ".join(dish['ingredients']))
        st.write("---")
        st.info("想再換一個？再點上面嘅按鈕即可")
    else:
        st.info("點擊上面嘅按鈕，App 會隨機建議一個菜式畀你")

# ==================== Tab 2: 所有菜式 ====================
with tab2:
    st.header("📖 所有推薦菜式")

    for dish in DEFAULT_DISHES:
        with st.expander(dish['name']):
            st.write("**材料：**", ", ".join(dish['ingredients']))