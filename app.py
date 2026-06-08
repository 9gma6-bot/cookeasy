import streamlit as st
import random

st.set_page_config(page_title="🍳 煮易 CookEasy", page_icon="🍳", layout="wide")

recipes = [
    {"id": 1, "name": "蒜蓉蒸排骨", "category": "家常菜", "time": "25 分鐘", "difficulty": "簡單", "servings": "2-3 人",
     "ingredients": ["排骨 400g", "蒜蓉 4 瓣", "生抽 1.5 湯匙", "蠔油 1 湯匙", "糖 1 茶匙", "生粉 1 茶匙", "油 1 湯匙"],
     "steps": ["排骨切小塊，沖洗抹乾。", "加入所有調味料醃 15 分鐘。", "大火蒸 18-20 分鐘。", "取出淋熱油及蔥花。"],
     "tips": "排骨要醃夠時間先入味。"},
    {"id": 2, "name": "薑蔥蒸魚", "category": "家常菜", "time": "15 分鐘", "difficulty": "簡單", "servings": "2 人",
     "ingredients": ["新鮮魚 1 條（約 400g）", "薑 5 片", "蔥 2 條", "生抽 2 湯匙", "熱油 2 湯匙", "鹽 少許"],
     "steps": ["魚洗淨抹乾，碟底放薑。", "大火蒸 8-10 分鐘。", "取出放蔥絲，淋生抽同熱油。"],
     "tips": "魚一定要新鮮。"},
    {"id": 3, "name": "番茄炒蛋", "category": "快手菜", "time": "10 分鐘", "difficulty": "簡單", "servings": "2 人",
     "ingredients": ["雞蛋 3 隻", "番茄 2 個", "糖 1 茶匙", "鹽 少許", "油 適量"],
     "steps": ["番茄切塊，蛋打散。", "炒蛋盛起，炒番茄出汁。", "倒返蛋液炒勻。"],
     "tips": "番茄炒至出汁先落蛋。"},
    {"id": 4, "name": "蠔油生菜", "category": "快手菜", "time": "8 分鐘", "difficulty": "簡單", "servings": "2-3 人",
     "ingredients": ["生菜 1 棵", "蠔油 2 湯匙", "生抽 1 茶匙", "糖 半茶匙", "蒜蓉 2 瓣", "油 1 湯匙"],
     "steps": ["爆蒜蓉，放入生菜快炒。", "加入調味料炒勻即成。"],
     "tips": "火要猛，炒太耐會出水。"},
    {"id": 5, "name": "冬瓜排骨湯", "category": "湯水", "time": "40 分鐘", "difficulty": "簡單", "servings": "3-4 人",
     "ingredients": ["冬瓜 500g", "排骨 300g", "薑 3 片", "鹽 適量", "蔥 1 條"],
     "steps": ["排骨飛水。", "煲排骨 25 分鐘。", "落冬瓜再煲 10 分鐘。"],
     "tips": "可加陳皮或眉豆更清甜。"},
    {"id": 6, "name": "涼拌黃瓜", "category": "小菜", "time": "10 分鐘", "difficulty": "簡單", "servings": "2 人",
     "ingredients": ["黃瓜 2 條", "蒜蓉 3 瓣", "生抽 1 湯匙", "醋 1 湯匙", "糖 1 茶匙", "鹽 少許"],
     "steps": ["黃瓜拍扁切段醃 5 分鐘。", "加入所有調味料拌勻。"],
     "tips": "可放雪櫃更爽口。"},
    {"id": 7, "name": "豉汁蒸排骨", "category": "家常菜", "time": "25 分鐘", "difficulty": "簡單", "servings": "2-3 人",
     "ingredients": ["排骨 400g", "豆豉 1.5 湯匙", "蒜蓉 3 瓣", "生抽 1 湯匙", "蠔油 1 湯匙", "糖 半茶匙"],
     "steps": ["排骨用豆豉同調味料醃 15 分鐘。", "大火蒸 18-20 分鐘。"],
     "tips": "豆豉唔使洗，鹹香味更正。"},
    {"id": 8, "name": "蛋炒飯", "category": "快手菜", "time": "12 分鐘", "difficulty": "簡單", "servings": "2 人",
     "ingredients": ["白飯 2 碗（隔夜飯）", "雞蛋 2 隻", "蔥 1 條", "生抽 1 湯匙", "鹽 少許", "油 2 湯匙"],
     "steps": ["炒蛋盛起。", "炒飯加入生抽同鹽。", "最後落蛋同蔥花。"],
     "tips": "用隔夜飯炒會更香。"},
    {"id": 9, "name": "紅燒豆腐", "category": "家常菜", "time": "15 分鐘", "difficulty": "簡單", "servings": "2-3 人",
     "ingredients": ["豆腐 1 盒", "蒜蓉 2 瓣", "生抽 1.5 湯匙", "蠔油 1 湯匙", "糖 半茶匙", "水 100ml"],
     "steps": ["豆腐煎至金黃。", "加入調味料同水煮 5 分鐘收汁。"],
     "tips": "豆腐煎金黃先落汁更入味。"},
    {"id": 10, "name": "薑葱炒蟹", "category": "家常菜", "time": "20 分鐘", "difficulty": "中等", "servings": "2 人",
     "ingredients": ["蟹 2 隻", "薑 5 片", "蔥 3 條", "生抽 2 湯匙", "蠔油 1 湯匙", "糖 1 茶匙", "酒 1 湯匙"],
     "steps": ["爆薑蔥，放入蟹大火炒。", "加酒同調味料炒至蟹殼紅。"],
     "tips": "蟹要新鮮，炒至蟹殼變紅就熟。"}
]

st.title("🍳 煮易 CookEasy")
st.caption("解決每日煮食煩惱 · 適合新手")

tab1, tab2, tab3 = st.tabs(["📅 今日建議", "📖 所有菜式", "🍲 湯水類"])

with tab1:
    st.header("📅 今日建議")
    if st.button("🔄 給我一個菜式建議", use_container_width=True):
        st.session_state["suggested"] = random.choice(recipes)
    if "suggested" in st.session_state:
        r = st.session_state["suggested"]
        with st.container(border=True):
            st.subheader(f"🍽️ {r['name']}")
            c1, c2, c3 = st.columns(3)
            c1.metric("時間", r['time'])
            c2.metric("難度", r['difficulty'])
            c3.metric("人數", r['servings'])
            st.markdown("**🧂 材料**")
            for i in r['ingredients']: st.write(f"- {i}")
            st.markdown("**📝 步驟**")
            for i, s in enumerate(r['steps'], 1): st.write(f"{i}. {s}")
            st.info(f"💡 {r['tips']}")

with tab2:
    st.header("📖 所有菜式")
    search = st.text_input("🔍 搜尋", "")
    diff = st.selectbox("難度", ["全部"] + sorted(set(r['difficulty'] for r in recipes)))
