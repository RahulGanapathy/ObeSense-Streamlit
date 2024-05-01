import streamlit as st
import pickle
import pandas as pd
from streamlit_extras.app_logo import add_logo

custom_css = """
<style>
    header.st-emotion-cache-1avcm0n.ezrtsby2, section.main.st-emotion-cache-uf99v8.ea3mdgi8{
        background-color:#0c0c0c;
    }

    section.st-emotion-cache-1cypcdb.eczjsme11{
        background-color:#212121;
    }

    div.st-emotion-cache-zq5wmm.ezrtsby0, button.st-emotion-cache-e370rw.e1vs0wn31{
        visibility: hidden;
    }

    [data-testid="stSidebarNav"] {
        padding-top: 200px;
        margin-left: 10px;
        width:310px;
    }

    div.stMarkdown{
        font-size: 40px;
        font-weight: bold;
        color: #0b7b9e;
    }

    div.st-emotion-cache-1v0mbdj.e115fcil1{
        position: relative;
        left:40%;
    }

    button.st-emotion-cache-19rxjzo.ef3psqc12{
        position:relative;
        left:50%;
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

st.image("logo.ico")

model = pickle.load(open('./classifier.pkl','rb'))
encoder = pickle.load(open('./encoder.pkl','rb'))

Age = st.number_input("Enter your Age:",step=1)
Gender = st.radio(
    'Your Gender:',
    ['Male', 'Female']
)
Height = st.number_input("Enter your Height in m:",step=0.01)
Weight = st.number_input("Enter your Weight:",step=0.1)
CALC = st.selectbox(
    "How often do you drink alcohol?",
    ['Always','Frequently','Sometimes','Never']
)
FAVC = st.radio(
    "Do you eat high caloric food frequently?",
    ['Yes','No']
)
NCP = st.number_input("How many main meals do you have daily?",step=1)
SCC = st.radio(
    "Do you monitor the calories you eat daily?",
    ['Yes','No']
)
SMOKE = st.radio(
    "Do you smoke?",
    ['Yes','No']
)
CH2O = st.number_input("How much water do you drink daily?",step=0.1)
family_history_with_overweight = st.radio(
    "Does your family has history with overweight?",
    ['Yes','No']
)
FAF = st.number_input("How often do you have physical activity?",step=1)
TUE = st.number_input("How much time do you spend on cell phone and other devices?",step=0.1)
CAEC = st.selectbox(
    "Do you eat any food between meals?",
    ['Always','Frequently','Sometimes','Never']
)
MTRANS = st.selectbox(
    "Which transportation do you usually use?",
    ['Walk','Cycle','Bike','Car','Public Transportation']
)

data = pd.DataFrame({'Age':Age,'Gender':Gender,'Height':Height,'Weight':Weight,'CALC':CALC,'FAVC':FAVC,'NCP':NCP,'SCC':SCC,'SMOKE':SMOKE,'CH2O':CH2O,'family_history_with_overweight':family_history_with_overweight,'FAF':FAF,'TUE':TUE,'CAEC':CAEC,'MTRANS':MTRANS}, index=[0])

if st.button("Predict"):
    pred = model.predict(data)
    st.write('Status: ',encoder.inverse_transform(pred)[0])