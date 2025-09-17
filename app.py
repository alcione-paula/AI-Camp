import streamlit as st
from agent import chamar_agente

st.set_page_config(page_title="Chat com Agente IA", layout="centered")

st.title("🤖 Chat com Agente StackSpot IA")

if "history" not in st.session_state:
    st.session_state.history = []

# Caixa de entrada
msg = st.chat_input("Digite sua mensagem...")

if msg:
    st.session_state.history.append(("Você", msg))
    resposta = chamar_agente(msg)
    st.session_state.history.append(("Agente", resposta))

# Exibir histórico do chat
for sender, text in st.session_state.history:
    if sender == "Você":
        st.chat_message("user").markdown(text)
    else:
        st.chat_message("assistant").markdown(text)
