import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page

custom_css = """
<style>
    header.st-emotion-cache-1avcm0n.ezrtsby2, section.main.st-emotion-cache-uf99v8.ea3mdgi8{
        background-color:#0c0c0c;
    }

    section.st-emotion-cache-1cypcdb.eczjsme11{
        background-color:#212121;
    }

    div.st-emotion-cache-zq5wmm.ezrtsby0{
        visibility: hidden;
    }

    [data-testid="stSidebarNav"] {
        padding-top: 200px;
        margin-left: 10px;
        width:310px;
    }

    button.st-emotion-cache-19rxjzo.ef3psqc12{
        color:#035b7a;
        background-color: #dddace;
    }
</style>
"""

st.set_page_config(
    page_title="ObeSense",
    page_icon="logo.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

add_logo("logo.ico")

st.markdown(custom_css,unsafe_allow_html=True)

st.title("ObeSense")

st.write("Introducing ObeSense: our web application harnesses machine learning to classify obesity levels based on user data."
         "Experience the precision of our RandomForestClassifier model as it empowers you with personalized insights for a healthier lifestyle."
         "Discover ObeSense for accurate predictions and tailored recommendations to support your well-being journey.")

if st.button("Begin"):
    switch_page("classifier")