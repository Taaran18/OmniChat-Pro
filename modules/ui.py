import streamlit as st
from modules.tools import format_chat_for_download


def render_sidebar(ai_service):
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=80)
        st.title("OmniChat Pro")
        model_name = st.selectbox(
            "AI Brain", options=list(ai_service.models.keys()), index=7
        )
        st.divider()
        st.subheader("Personalization")
        system_prompt = st.text_area(
            "AI Personality",
            value="You are a helpful and professional AI assistant.",
            height=100,
        )
        temperature = st.slider(
            "Creativity (Temperature)",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
        )
        st.divider()
        st.subheader("Knowledge")
        uploaded_file = st.file_uploader(
            "Upload Context (PDF/TXT)", type=["pdf", "txt"]
        )
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Refresh", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
        with col2:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
        if "messages" in st.session_state and st.session_state.messages:
            chat_text = format_chat_for_download(st.session_state.messages, model_name)
            st.download_button(
                label="📥 Download Export",
                data=chat_text,
                file_name=f"chat_{model_name}.txt",
                mime="text/plain",
                use_container_width=True,
            )
        return model_name, system_prompt, temperature, uploaded_file


def render_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "tokens" in message:
                st.caption(
                    f"Tokens: {message['tokens']} | Cost: ${message['cost']:.5f}"
                )
