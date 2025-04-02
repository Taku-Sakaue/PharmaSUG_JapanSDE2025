import streamlit as st

st.markdown('---')
st.markdown('#### - checkbox')
st.code('st.checkbox("ON")', language='python')
st.checkbox('ON')


st.markdown('---')
st.markdown('#### - feedback')
st.code('st.feedback("faces")', language='python')
st.feedback("faces")

st.markdown('---')
st.markdown('#### - radio')
st.code('st.radio("Select", ["ON", "OFF"])', language='python')
st.radio("Select", ["ON", "OFF"])

st.markdown('---')
st.markdown('#### - Toggle')
st.code('st.toggle("Enable")', language='python')
st.toggle("Enable")

st.markdown('---')
st.markdown('#### - Selectbox')
st.code('st.selectbox("Select", ["A", "B"])', language='python')
st.selectbox("Select", ["A", "B"])

st.markdown('---')
st.markdown('#### - Slider')
st.code('st.slider("Pick a number", 0, 100)', language='python')
st.slider("Pick a number", 0, 100)

st.markdown('---')
st.markdown('#### - Text ipnut')
st.code('st.text_input("Input your text")', language='python')
st.text_input("Input your text")

st.markdown('---')
st.markdown('#### - Multiple line text ipnut')
st.code('st.text_area("Input your text")', language='python')
st.text_area("Input your text")

st.markdown('---')
st.markdown('#### - Number input')
st.code('st.number_input("Pick a number", 0, 10)', language='python')
st.number_input("Pick a number", 0, 10)

st.markdown('---')
st.markdown('#### - Date input')
st.code('st.date_input("Input date")', language='python')
st.date_input("Input date")

st.markdown('---')
st.markdown('#### - Time input')
st.code('st.time_input("Input time")', language='python')
st.time_input("Input time")

st.markdown('---')
st.markdown('#### - File upload')
st.code('st.file_uploader("Upload your file")', language='python')
st.file_uploader("Upload your file")

#st.markdown('---')
#st.markdown('#### - Take picture')
#st.camera_input("Take a picture")


st.markdown('---')
st.markdown('#### - クルクル')
st.code('''
with st.spinner(text="考え中"):
    time.sleep(3)
    st.success("Done")
''', language='python')
if(st.button('クルクル')):
	with st.spinner(text="考え中"):
		time.sleep(3)
		st.success("Done")


st.markdown('---')
st.markdown('#### - progress bar')
st.code('''
pbar = st.progress(50)
time.sleep(3)
pbar.progress(100)
''', language='python')

if(st.button('progress bar')):
	pbar = st.progress(50)
	time.sleep(3)
	pbar.progress(100)
