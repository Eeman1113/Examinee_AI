import streamlit as st 
import openai
import re
# import pywhatkit as kit
# import cv2

# def write_me(a):
#     for i in range(0,len(a)):
#         enter_what_you_want_to_write = a[i]
#         kit.text_to_handwriting(enter_what_you_want_to_write, save_to="handwriting{}.png".format(i))
#         img = cv2.imread("/Users/eemanmajumder/code_shit/Examinee_AI/Image/handwriting{}.png".format(i))
#         cv2.imshow(img)
#         st.markdown("___")
#         st.image("/Users/eemanmajumder/code_shit/Examinee_AI/Image/handwriting{}.png".format(i))

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

st.markdown("<h1 style='text-align: center; '>Ansar Kun 解</h1>", unsafe_allow_html=True)
a=st.text_input("Enter array of questions: ")


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
    







st.write(c)
st.balloons()
# write_me(c)





