#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 16:14:39 2023

@author: rajankumar
"""
import streamlit as st
import openai

st.title("Chatting with ChatGPT when chatgpt will be answering like shakespeare")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    )
model_engine = "text-davinci-003"
openai.api_key = "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"
def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Enter query here")
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        messages =  [  
        {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
        {'role':'user', 'content':user_query}
        ]
        response = get_completion_from_messages(messages, temperature=1)
        return st.write(f"{response}")

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
main()
        





