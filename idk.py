import streamlit as st
import info

def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("---")
about_me_section()

def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linked_url}"><img src="{info.linkedin_url}" alt="Linkedin" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{info.my_linked_url}"><img src="{info.linkedin_url}" alt="Linkedin" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="{info.my_linked_url}"><img src="{info.linkedin_url}" alt="Linkedin" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    #links_section()
