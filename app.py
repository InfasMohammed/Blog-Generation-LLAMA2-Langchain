import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


## function for LLMA 2 Model

def getLLamaresponse(input_text,no_words,blog_style):
     
     ## LLama model 

     llm=CTransformers(model='Model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                       model_type='llama',
                       config={'max_new_tokens':256,
                               'temperature':0.01})
     

     ## prompt templet

     template = """
                Write a blog for {blog_style} job profile for a topic {input_text}
                within {no_words} words.
                """

     prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                         template=template)
     

     ## Generate response from the llama 2 model

     response=llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
     print(response)
     return response





st.set_page_config(page_title="Generate Blog",
                   page_icon=":memo:",
                   layout='wide'
                   )

st.header("Generate Blog")

input_text=st.text_input("Enter the blog topic")

## creating to more coloumn for additional 2 fileds

col1,col2=st.columns([5,5])

with col1:
     no_words=st.text_input("No of words")
with col2:
     blog_style=st.selectbox('Wrting the blogs for',('Researchers','Data Scientist','Common people'), index=0)


submit=st.button("Generate")


## final response

if submit:
     st.write(getLLamaresponse(input_text,no_words,blog_style))
