

import streamlit as st
import json
import pandas as pd


def welcome_section():
    st.header("Spider Man")
    st.write("Welcome to the Spider Man Page! Here you can learn about the different Spider men!")
    st.write("---")
welcome_section()

def choose_your_spider():

    st.header("Choose your Spider Man")
    if st.button("Tom Holland"): #NEW
        st.write("Holland's first appearance as Spider Man was in the 2016 Marvel Movie, Civil War. Since then, Holland has been in 6 movies as Spider Man. A new Spider Man movie featuring him is predicted to be released in 2026.")
    if st.button("Andrew Garfield"):
        st.write("Garfield's first appearance as Spider Man was in the 2012 movie with Emma Stone. Garfield released 3 total Spider Man movies.")
    if st.button("Toby Maguire"):
        st.write("Maguire's first appearance as Spider Man was in the 2002 movie with Emma Stone. Garfield released 3 total Spider Man movies.")
choose_your_spider()



def select_your_multiverse():

    st.header("Which Earth do you Belong to?")
    num = st.slider("Choose your universe...", 0, 500) #NEW
    if num>=0 and num<=100:
        st.write("You're in the same world as T-rex Spiderman")
    elif num>100 and num<400:
        st.write("You're in the same world as Gwen Stacy")
    elif num>=400:
        st.write("You're in the same world as Miles Morales")
    st.write("---")
select_your_multiverse()

def show_earnings():
    st.header("Earnings Across Spider Men")
    inline = open("data.json")
    myData = json.load(inline)
    st.bar_chart(data=myData, x='movie', y='earnings', color='#CC5500') #NEW
show_earnings()
