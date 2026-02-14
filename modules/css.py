import streamlit as st


def inject_custom_css():
    st.markdown(
        """
    <style>
        :root {
            --bg-color: #FFFFFF;
            --text-color: #31333F;
            --sidebar-bg: #F8F9FB;
            --bubble-bg-user: rgba(74, 144, 226, 0.12);
            --bubble-bg-ai: rgba(0, 0, 0, 0.02);
            --border-color: rgba(0, 0, 0, 0.06);
            --input-bg: #F0F2F6;
            --dropdown-bg: #FFFFFF;
        }
        @media (prefers-color-scheme: dark) {
            :root {
                --bg-color: #0E1117;
                --text-color: #FAFAFA;
                --sidebar-bg: #1A1C23;
                --bubble-bg-user: rgba(74, 144, 226, 0.2);
                --bubble-bg-ai: rgba(255, 255, 255, 0.04);
                --border-color: rgba(255, 255, 255, 0.08);
                --input-bg: #262730;
                --dropdown-bg: #262730;
            }
        }
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"] {
            background-color: var(--bg-color) !important;
            color: var(--text-color) !important;
            transition: all 0.2s ease;
        }
        [data-testid="stSidebar"] {
            background-color: var(--sidebar-bg) !important;
            border-right: 1px solid var(--border-color);
        }
        [data-testid="stSidebar"] section {
            padding-top: 1rem !important;
        }
        [data-testid="stHeader"] {
            background-color: transparent !important;
        }
        .main-header {
            font-size: 2.2rem;
            font-weight: 800;
            text-align: center;
            background: linear-gradient(90deg, #00C6FF, #0072FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            padding-top: 0.2rem;
        }
        [data-testid="stChatMessage"] {
            border-radius: 12px;
            padding: 0.6rem 1rem;
            margin-bottom: 0.4rem;
            border: 1px solid var(--border-color);
            background-color: var(--bubble-bg-ai) !important;
        }
        [data-testid="stChatMessage"][data-testid="stChatMessage-user"] {
            background-color: var(--bubble-bg-user) !important;
        }
        [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] span {
            color: var(--text-color) !important;
            font-size: 0.95rem;
            line-height: 1.4;
        }
        [data-testid="stChatInput"] {
            background-color: var(--input-bg) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 15px !important;
            color: var(--text-color) !important;
        }
        [data-testid="stChatInput"] textarea {
            background-color: transparent !important;
            color: var(--text-color) !important;
            padding: 0.5rem !important;
        }
        [data-testid="stBottomBlockContainer"] {
            background-color: var(--bg-color) !important;
            padding-bottom: 1.5rem;
        }
        div[data-baseweb="select"] > div, div[data-baseweb="popover"] {
            background-color: var(--dropdown-bg) !important;
            color: var(--text-color) !important;
            border: 1px solid var(--border-color) !important;
        }
        div[data-testid="stSelectbox"] div, div[data-testid="stSelectbox"] label {
            color: var(--text-color) !important;
        }
        .stButton > button {
            padding: 0.25rem 0.5rem !important;
            min-height: 2rem !important;
        }
        #MainMenu, footer, [data-testid="stDecoration"] {visibility: hidden;}
    </style>
    """,
        unsafe_allow_html=True,
    )
