"""SENG 481 - P02: Yerelde çalışan açık kaynak LLM ile basit chatbot.

Çalıştırmak için:
    1. Ollama kurulu ve çalışıyor olmalı (https://ollama.com)
    2. ollama pull llama3.2:3b
    3. pip install -r requirements.txt
    4. streamlit run app.py
"""

import ollama
import streamlit as st

DEFAULT_SYSTEM_PROMPT = (
    "Sen Türkçe konuşan, kibar ve yardımsever bir asistansın. "
    "Cevaplarını kısa ve anlaşılır tut."
)


def get_local_models() -> list[str]:
    """Bilgisayarda yüklü Ollama modellerini listeler."""
    try:
        response = ollama.list()
        return [m.model for m in response.models]
    except Exception:
        return []


st.set_page_config(page_title="Yerel Chatbot", page_icon="💬")
st.title("💬 Yerel LLM Chatbot")

# --- Kenar çubuğu: ayarlar ---
with st.sidebar:
    st.header("Ayarlar")
    models = get_local_models()
    if not models:
        st.error(
            "Ollama'ya bağlanılamadı veya yüklü model yok.\n\n"
            "Ollama'nın çalıştığından emin olun ve örneğin "
            "`ollama pull llama3.2:3b` komutunu çalıştırın."
        )
        st.stop()

    model = st.selectbox("Model", models)
    system_prompt = st.text_area("Sistem promptu", DEFAULT_SYSTEM_PROMPT, height=120)

    if st.button("Sohbeti temizle"):
        st.session_state.messages = []
        st.rerun()

# --- Sohbet geçmişi ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Yeni mesaj ---
if prompt := st.chat_input("Mesajınızı yazın..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    full_history = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    with st.chat_message("assistant"):
        def stream():
            for chunk in ollama.chat(model=model, messages=full_history, stream=True):
                yield chunk["message"]["content"]

        answer = st.write_stream(stream())

    st.session_state.messages.append({"role": "assistant", "content": answer})
