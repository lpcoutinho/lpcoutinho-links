import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

# st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('me.jpeg'))

st.header('Luiz Paulo Coutinho, Developer')

st.info('Python developer, passionate about web solutions, devops culture and data analysis.')

icon_size = 20

# st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
# st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)

st_button('medium', 'https://www.medium.com/@coutinholps', 'Read my Posts', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/luizpaulocoutinho/', 'Follow me on LinkedIn', icon_size)
st_button('git', 'https://github.com/lpcoutinho', 'See my Git', icon_size)