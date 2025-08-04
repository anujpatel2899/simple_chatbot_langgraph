import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage


config = {"configurable":{"thread_id":"thread-1"}}

# st.session_state -> dict -> enter do not erase

if "message_history" not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history 
for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])
user_input = st.chat_input("Type here")

if user_input:
    # first add message to message_history
    st.session_state['message_history'].append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # Second add message to message_history
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {"messages":[HumanMessage(content=user_input)]},
                config=config,
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append({"role":"assistant","content":ai_message})    




