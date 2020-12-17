import numpy as np
import pandas as pd
import streamlit as st
import time
from os import path
from os import remove
import pickle
from urllib.request import urlopen
import cloudpickle as cp

st.set_page_config(
    page_title="PCA",
    page_icon="🐍",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_rf_model():
    RF_IE_Model = pickle.load(open("notebooks/models/RF_IE_Model_2.0", 'rb'))
    RF_JP_Model = pickle.load(open("notebooks/models/RF_JP_Model_2.0", 'rb'))
    RF_NS_Model = pickle.load(open("notebooks/models/RF_NS_Model_2.0", 'rb'))
    RF_TF_Model = pickle.load(open("notebooks/models/RF_TF_Model_2.0", 'rb'))
    return RF_IE_Model, RF_JP_Model, RF_NS_Model, RF_TF_Model
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_bert_model():
    bert = cp.load(urlopen("https://drive.google.com/file/d/1U03uM8J360eoB06pnmgEDlZEYj5_qm10/view?usp=sharing", 'rb'))
    return bert

rf_models = load_rf_model()
bert_model = load_bert_model()

st.sidebar.markdown(f"""
    # Header resizer
    """)

font_size = st.sidebar.slider('Changer header size', 16, 72, 36)

FONT_SIZE_CSS = f"""
<style>
h1 {{
    font-size: {font_size}px !important;
}}
</style>
"""
st.write(FONT_SIZE_CSS, unsafe_allow_html=True)

st.markdown("""
    # Personality Chat Assistant

    ## Please upload your target text

""")
st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose a text file", type="txt")

if uploaded_file is not None:
    data = uploaded_file
    st.write(data)
    with open('data.txt', 'w') as f:
        f.write('data')

st.markdown("""
    ## Do you want our model to base on your data?(which is time consuming)

""")

@st.cache(suppress_st_warning=True)
def fine_tune(uploaded_file):
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)


    bar.empty()
    latest_iteration.empty()

if st.checkbox('Yes&Finetune'):
    if path.exists('data.txt'):
        with open('data.txt', 'r') as f:
            if(str(f.read()) == 'data'):
                st.write('Our model is finetuned based on your data')
                'Starting a long computation...'
                fine_tune(uploaded_file)
                latest_iteration = st.empty()
                latest_iteration.text(f'Iteration 100')
                bar = st.progress(100)
                '...and now we\'re done!'
    else:
        st.write('''
    Please upload a txt file
    ''')

if st.button('Classification'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write('Target Personality type is blah..., click here to see more https://cn.pornhub.com')
    # st.write('Further clicks are not visible but are executed')

if path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        if(str(f.read()) == 'data'):
            st.write('Target Personality type is blah..., click here to see more https://cn.pornhub.com')


st.markdown("""
    ## Now give us your prompt text and see what we can do

""")
txt = st.text_area('Text to analyze', '''

    ''')
if st.button('Generate text'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write(f'{txt} blahblahblah I am handsome 🔞')

if path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        if(str(f.read()) == 'data'):
                st.write(f'{txt} blahblahblah I am handsome 🔞')

if st.button('More 🎈🎈🎈 please!'):
    st.balloons()

if st.button('Remove all'):
    if path.exists('data.txt'):
        remove('data.txt')
        'Already clean'
    else:
        'Already clean!!!!!!!!!!!!!!!!!!!!!!!🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕'
