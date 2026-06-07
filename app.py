import streamlit as st
import random

st.set_page_config(page_title="煮易 CookEasy", page_icon="🍳", layout="wide")
st.title("🍳 煮易 CookEasy")
st.subheader("解決每日煮食煩惱")

# ==================== 內置菜式庫 ====================
DEFAULT_DISHES = [
    # 原有 15 個
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

    # 新增 30 個家常便飯
    {"name": "豉油雞", "ingredients": ["雞", "生抽", "老抽", "薑"]},
    {"name": "蔥油雞", "ingredients": ["雞", "蔥", "薑", "生抽"]},
    {"name": "梅菜扣肉", "ingredients": ["五花肉", "梅菜", "生抽", "冰糖"]},
    {"name": "紅燒獅子頭", "ingredients": ["豬肉", "薑", "蔥", "生抽"]},
    {"name": "糖醋排骨", "ingredients": ["排骨", "糖", "醋", "生抽"]},
    {"name": "可樂雞翅", "ingredients": ["雞翅", "可樂", "生抽", "老抽"]},
    {"name": "黃金蛋炒飯", "ingredients": ["飯", "蛋", "蔥", "火腿"]},
    {"name": "XO醬炒蘆筍", "ingredients": ["蘆筍", "XO醬", "蒜蓉"]},
    {"name": "蒜蓉炒菜心", "ingredients": ["菜心", "蒜蓉", "生抽"]},
    {"name": "蠔油燴三菇", "ingredients": ["蘑菇", "蠔油", "蒜蓉"]},
    {"name": "豆豉炒四季豆", "ingredients": ["四季豆", "豆豉", "蒜蓉"]},
    {"name": "辣椒炒肉", "ingredients": ["豬肉", "青椒", "紅椒", "豆豉"]},
    {"name": "回鍋肉", "ingredients": ["五花肉", "青椒", "豆瓣醬"]},
    {"name": "宮保雞丁", "ingredients": ["雞肉", "花生", "乾辣椒", "生抽"]},
    {"name": "左宗棠雞", "ingredients": ["雞腿", "乾辣椒", "糖", "醋"]},
    {"name": "酸菜魚", "ingredients": ["魚", "酸菜", "辣椒", "薑"]},
    {"name": "水煮牛肉", "ingredients": ["牛肉", "豆芽", "辣椒", "花椒"]},
    {"name": "香菇滑雞", "ingredients": ["雞", "冬菇", "蠔油", "生抽"]},
    {"name": "薑汁撞奶", "ingredients": ["牛奶", "薑汁", "糖"]},
    {"name": "椰汁西米露", "ingredients": ["西米", "椰奶", "糖"]},
    {"name": "紅豆沙", "ingredients": ["紅豆", "糖", "椰奶"]},
    {"name": "綠豆沙", "ingredients": ["綠豆", "糖", "薑"]},
    {"name": "皮蛋瘦肉粥", "ingredients": ["米", "皮蛋", "瘦肉", "薑"]},
    {"name": "魚片粥", "ingredients": ["米", "魚片", "薑", "蔥"]},
    {"name": "艇仔粥", "ingredients": ["米", "花生", "腸", "蝦"]},
    {"name": "叉燒包", "ingredients": ["叉燒", "麵粉", "糖"]},
    {"name": "糯米雞", "ingredients": ["糯米", "雞", "冬菇", "蝦"]},
    {"name": "蘿蔔糕", "ingredients": ["白蘿蔔", "米粉", "臘腸"]},
    {"name": "腸粉", "ingredients": ["米粉", "蝦", "叉燒", "蔥"]},
    {"name": "牛腩粉", "ingredients": ["牛腩", "河粉", "薑", "八角"]},
]

# ==================== 煲湯水 ====================
SOUPS = [
    {"name": "老火靚湯", "ingredients": ["瘦肉", "紅蘿蔔", "玉米", "紅棗"]},
    {"name": "冬菇瘦肉湯", "ingredients": ["瘦肉", "冬菇", "紅棗", "薑"]},
    {"name": "花膠瘦肉湯", "ingredients": ["花膠", "瘦肉", "紅棗", "薑"]},
    {"name": "海帶排骨湯", "ingredients": ["排骨", "海帶", "紅棗", "薑"]},
    {"name": "羅漢果瘦肉湯", "ingredients": ["瘦肉", "羅漢果", "紅棗", "南北杏"]},
    {"name": "雪梨燉豬展", "ingredients": ["豬展", "雪梨", "南北杏", "紅棗"]},
    {"name": "木瓜燉魚尾", "ingredients": ["魚尾", "木瓜", "紅棗", "薑"]},
    {"name": "淮山杞子燉雞", "ingredients": ["雞", "淮山", "杞子", "紅棗"]},
    {"name": "黨參紅棗燉雞", "ingredients": ["雞", "黨參", "紅棗", "薑"]},
    {"name": "苦瓜排骨湯", "ingredients": ["排骨", "苦瓜", "紅棗", "薑"]},
]

# 合併所有菜式
ALL_DISHES = DEFAULT_DISHES + SOUPS

# ==================== 主畫面 ====================
tab1, tab2, tab3 = st.tabs(["📅 今日建議", "📖 所有菜式", "🍲 煲湯水"])

# ==================== Tab 1: 今日建議 ====================
with tab1:
    st.header("📅 今日建議")

    if st.button("🔄 隨機建議一個菜式", use_container_width=True):
        suggested = random.choice(ALL_DISHES)
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
    st.header("📖 所有推薦菜式（45 款）")

    for dish in DEFAULT_DISHES:
        with st.expander(dish['name']):
            st.write("**材料：**", ", ".join(dish['ingredients']))

# ==================== Tab 3: 煲湯水 ====================
with tab3:
    st.header("🍲 煲湯水（10 款）")

    for soup in SOUPS:
        with st.expander(soup['name']):
            st.write("**材料：**", ", ".join(soup['ingredients']))