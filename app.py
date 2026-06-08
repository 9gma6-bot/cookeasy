with tab2:
    st.header("📖 所有菜式")
    diff = st.selectbox("📊 難度篩選", ["全部"] + sorted(set(r['difficulty'] for r in recipes)))
    filtered = recipes if diff == "全部" else [r for r in recipes if r['difficulty'] == diff]
    for r in filtered:
        with st.expander(f"🍽️ {r['name']} ({r['time']} · {r['difficulty']})"):
            st.write(f"**時間**: {r['time']}　**難度**: {r['difficulty']}　**人數**: {r['servings']}")
            st.markdown("**🧂 材料**")
            for i in r['ingredients']: st.write(f"- {i}")
            st.markdown("**📝 步驟**")
            for i, s in enumerate(r['steps'], 1): st.write(f"{i}. {s}")
            st.success(f"💡 {r['tips']}")

with tab3:
    st.header("🍲 湯水類")
    soup = [r for r in recipes if "湯" in r['name'] or r['category'] == "湯水"]
    for r in soup:
        with st.expander(f"🍲 {r['name']}"):
            st.write(f"**時間**: {r['time']}　**難度**: {r['difficulty']}")
            for i in r['ingredients']: st.write(f"- {i}")
            for i, s in enumerate(r['steps'], 1): st.write(f"{i}. {s}")
            st.info(f"💡 {r['tips']}")
