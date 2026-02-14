import streamlit as st
import os

st.set_page_config(
    page_title="OmniChat Pro",
    page_icon="🤖",
    layout="wide",
)

from modules.ai import AIService
from modules.css import inject_custom_css
from modules.ui import render_sidebar, render_chat_history
from modules.tools import generate_chat_title, count_tokens, calculate_cost
from modules.docs import process_uploaded_file

if not os.getenv("OPENAI_API_KEY"):
    st.warning(
        "⚠️ OpenAI API Key not found. Please set it in your .env file or Streamlit Secrets."
    )
    st.stop()
if "ai_service" not in st.session_state:
    st.session_state.ai_service = AIService()

if "messages" not in st.session_state:
    st.session_state.messages = []

inject_custom_css()

model_name, sys_prompt, temp, doc_file = render_sidebar(st.session_state.ai_service)

st.markdown('<div class="main-header">OmniChat Pro</div>', unsafe_allow_html=True)

render_chat_history()

if prompt := st.chat_input("Message the AI..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        context = ""
        if doc_file:
            context = process_uploaded_file(doc_file)

        active_messages = [
            {"role": "system", "content": f"{sys_prompt}\n\nContext:\n{context}"}
        ]
        active_messages.extend(
            [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            for chunk in st.session_state.ai_service.get_chat_response(
                active_messages, model_name=model_name, temperature=temp, stream=True
            ):
                full_response += chunk
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

            tokens = count_tokens(full_response)
            cost = calculate_cost(tokens, model_name)
            st.caption(f"Tokens: {tokens} | Cost: ${cost:.5f}")

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response,
                    "tokens": tokens,
                    "cost": cost,
                }
            )

            if len(st.session_state.messages) <= 2:
                new_title = generate_chat_title(st.session_state.messages)
                st.session_state.chat_title = new_title

    except Exception as e:
        st.error(f"Error: {e}")
