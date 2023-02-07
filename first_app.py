# <pythonfile>.ipynb notebook
# 프로그램 작성시에는 <pythonfile>.py
# python3 <pythonfile>.py
# streamlit run <streamlitapp>.py 

import streamlit as st
import pandas as pd
import numpy as np
# pip install pandas
# conda install pandas

def text():
    #Mark Down
    st.markdown('아지야 뭐하니')
    st.markdown('Streamlit is **_really_ cool**.')
    st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

def dataframe1():
    df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))
    st.dataframe(df) # Same as st.write(df)

def temp_map():
    # 온도 출력
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    # 위도 경도에 맞는 지도를 출력
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(df)


def main():
    st.title("First_APP")

    st.sidebar.write('''
    # lab1
    # lab2
    - lab3
    - lab4
    ''')

    df = pd.DataFrame({
        "first_col":[1, 2, 3, 4],
        "second_col":[10, 20, 30, 40]
    })
    st.write(df)

    text()

    if st.checkbox("show dataframe"):
        dataframe1()

    temp_map()

if __name__ == "__main__":
    main()
    
import random
import datetime

st.title(':sparkles:로또 생성기:sparkles:')


def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto

# st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
# st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button('로또를 생성해 주세요!')

if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")    
    
    
<div class="group_nav">
<ul class="list_nav type_fix">
<li class="nav_item">
<a href="https://mail.naver.com/" class="nav" data-clk="svc.mail"><i class="ico_mail"></i>메일</a>
</li>
<li class="nav_item"><a href="https://section.cafe.naver.com/" class="nav" data-clk="svc.cafe">카페</a></li>
<li class="nav_item"><a href="https://section.blog.naver.com/" class="nav" data-clk="svc.blog">블로그</a></li>
<li class="nav_item"><a href="https://kin.naver.com/" class="nav" data-clk="svc.kin">지식iN</a></li>
<li class="nav_item"><a href="https://shopping.naver.com/" class="nav shop" data-clk="svc.shopping"><span class="blind">쇼핑</span></a></li>
<li class="nav_item"><a href="https://shoppinglive.naver.com/home" class="nav shoplive" data-clk="svc.shoppinglive"><span class="blind">쇼핑
<li class="nav_item"><a href="https://order.pay.naver.com/home" class="nav" data-clk="svc.pay">Pay</a></li>
<li class="nav_item">
<a href="https://tv.naver.com/" class="nav" data-clk="svc.tvcast"><i class="ico_tv"></i>TV</a>
</li>
</ul>
<ul class="list_nav NM_FAVORITE_LIST">
<li class="nav_item"><a href="https://dict.naver.com/" class="nav" data-clk="svc.dic">사전</a></li>    
