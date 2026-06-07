import streamlit as st
import json
import os
import random

st.set_page_config(page_title="煮易 CookEasy", page_icon="🍳")
st.title("🍳 煮易 CookEasy")
st.subheader("解決每日煮食煩惱")

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

FAMILY_FILE = os.path.join(DATA_DIR, "family.json")
MY_DISHES_FILE = os.path.join(DATA_DIR, "my_dishes.json")

def load_family():
    if os.path.exists(FAMILY_FILE):
        with open(FAMILY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_family(family):
    with open(FAMILY_FILE, "w", encoding="utf-8") as f:
        json.dump(family, f, ensure_ascii=False, indent=2)

def load_my_dishes():
    if os.path.exists(MY_DISHES_FILE):
        with open(MY_DISHES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_my_dishes(dishes):
    with open(MY_DISHES_FILE, "w", encoding="utf-8") as f:
        json.dump(dishes, f, ensure_ascii=False, indent=2)

# Sidebar - 家庭成員
st.sidebar.header("👨‍👩‍👧‍👦 家庭成員")
family = load_family()

with st.sidebar.form("add_member"):
    name = st.text_input("成員名稱")
    dislikes = st.text_input("唔鍾意/過敏（用逗號分隔）")
    if st.form_submit_button("新增成員"):
        if name:
            family.append({"name": name, "dislikes": dislikes})
            save_family(family)
            st.rerun()

if family:
    st.sidebar.write("目前成員：")
    for member in family:
        st.sidebar.write(f"- {member['name']}")

# 主頁面 tabs
tab1, tab2, tab3 = st.tabs(["📅 今日建議", "📖 我的菜式庫", "👨‍👩‍👧‍👦 家庭設定"])

with tab1:
    st.header("📅 今日建議")
    dishes = load_my_dishes()
    if dishes and family:
        suggested = random.choice(dishes)
        st.success(f"**今日建議：{suggested['name']}**")
        st.write("材料：", ", ".join(suggested['ingredients']))
        
        if st.button("換另一個建議"):
            st.rerun()
    else:
        st.info("請先喺「我的菜式庫」新增至少一個菜式，同埋喺側邊欄新增家庭成員")

with tab2:
    st.header("📖 我的菜式庫")
    
    with st.form("add_dish"):
        dish_name = st.text_input("菜式名稱（例如：蒜蓉蒸排骨）")
        ingredients_input = st.text_input("材料（用逗號分隔，例如：排骨,蒜蓉,生抽）")
        if st.form_submit_button("新增菜式"):
            if dish_name and ingredients_input:
                dishes = load_my_dishes()
                dishes.append({
                    "name": dish_name,
                    "ingredients": [i.strip() for i in ingredients_input.split(",")]
                })
                save_my_dishes(dishes)
                st.success(f"已新增：{dish_name}")
                st.rerun()
    
    dishes = load_my_dishes()
    if dishes:
        st.write("你已儲存嘅菜式：")
        for d in dishes:
            st.write(f"- **{d['name']}**：{', '.join(d['ingredients'])}")
    else:
        st.info("你仲未新增任何菜式，快啲喺上面新增啦！")

with tab3:
    st.header("家庭設定（開發中）")
    st.write("之後會加入更多家庭管理功能")