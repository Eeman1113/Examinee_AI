#___________________________________________________________________________________________________________________

import streamlit as st 
import openai
import re

#___________________________________________________________________________________________________________________

def add_newlines_and_split(text):
    # Split the string into words
    words = text.split()
    
    # Add a newline character after every 5th word
    new_text = ""
    for i, word in enumerate(words):
        if (i+1) % 5 == 0:
            new_text += f"{word}\n"
        else:
            new_text += f"{word} "
    
    # Split the string into lines
    lines = new_text.split("\n")

    # Split the lines into chunks of 21
    chunks = [lines[i:i+21] for i in range(0, len(lines), 21)]
    
    # Join each chunk into a single string
    chunk_strings = ["\n".join(chunk) for chunk in chunks]

    return chunk_strings

#___________________________________________________________________________________________________________________

def group_elements(lst, n):
    lst = ["".join(lst[i:i+n]) for i in range(0, len(lst), n)]
    if len(lst) % 2 != 0:
        lst.append("")
    return lst

#___________________________________________________________________________________________________________________

def add_newline_after_question(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].replace('?', '?\n')
    return arr

#___________________________________________________________________________________________________________________

st.markdown("<h1 style='text-align: center; '>Ansar Chan (◕ヮ◕) 解</h1>", unsafe_allow_html=True)
a=st.text_input("Enter array of questions: ")

#___________________________________________________________________________________________________________________
q=re.split("[?.]",a)
q=q[:len(q)-1]
print(q)
c=[]
d=0
for i in q:
    openai.api_key = st.secrets['open_api']

    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=i+"?",
        temperature=0.7 ,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    d=d+1
    b=response
    # c.append(d)
    c.append(str(d)+". "+i+"?")
    c.append(response.choices[0].text)
    st.markdown('___')
    st.write(str(d)+". "+i+"?")
    print(str(d)+". "+i+"?")
    st.write("Ans: "+response.choices[0].text)

#___________________________________________________________________________________________________________________
st.write(c)
st.balloons()
#___________________________________________________________________________________________________________________
st.markdown("___")
title_text=add_newline_after_question(group_elements(c,2))
print(c)
for i in range(0,len(title_text)):

    title_text[i]=add_newlines_and_split(title_text[i])
    from PIL import Image, ImageFont, ImageDraw 
    for j in range(0,len(title_text[i])):
        img_k = Image.open("Image/Pages.png")
        title_font = ImageFont.truetype('fonts/Mynerve-Regular.ttf', 70)
        img = ImageDraw.Draw(img_k)
        img.text((100,100.3), title_text[i][j], (0,0,0), font=title_font)
        img_k.save("Image/result{}.png".format(i))
        st.image('Image/result{}.png'.format(i))

#___________________________________________________________________________________________________________________
