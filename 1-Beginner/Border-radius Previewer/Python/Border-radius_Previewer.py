import streamlit as st

st.set_page_config(page_title="Border-radius Previewer", page_icon="📐",
                   layout="centered")

st.title("📐 Border-radius Previewer")
st.write("Передвигайте ползунки, чтобы изменить форму блока.",
         " Готовый CSS-код можно скопировать ниже.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Настройка углов (px)")
    top_left = st.slider("Верхний-левый", min_value=0,
                         max_value=150, value=0)
    top_right = st.slider("Верхний-правый", min_value=0,
                          max_value=150, value=0)
    bottom_right = st.slider("Нижний-правый", min_value=0,
                             max_value=150, value=0)
    bottom_left = st.slider("Нижний-левый", min_value=0,
                            max_value=150, value=0)

css_style = f"border-radius: {top_left}px {top_right}px {bottom_right}px {bottom_left}px;"

with col2:
    st.subheader("Превью")
    st.markdown(
        f"""
        <div style="
            width: 200px;
            height: 200px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
            margin: 20px auto;
            {css_style}
            transition: border-radius 0.1s ease;
        "></div>
        """,
        unsafe_allow_html=True
    )

st.divider()


st.subheader("📋 Готовый CSS код:")
st.code(css_style, language="css")
