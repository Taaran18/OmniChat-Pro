# 🤖 OmniChat Pro

OmniChat is a high-performance, modular, and aesthetic conversational AI platform built with **Streamlit** and **OpenAI**. It features advanced capabilities like RAG-lite document processing, real-time streaming, and cost transparency, all wrapped in a premium adaptive UI.

## ✨ Key Features

- **⚡ Streaming Pro**: Real-time word-by-word response rendering for an elite UX.
- **📄 RAG-Lite Knowledge**: Upload `.pdf` or `.txt` files to provide context-aware grounding for the AI.
- **🌓 Auto-Theme Adaptive**: Native CSS detection for system light/dark modes with pixel-perfect contrast.
- **📊 Usage Transparency**: Real-time token counting and estimated cost calculation for every response.
- **🎭 Personality Forge**: Customizable system prompts to define AI behavior and identity.
- **📥 Topic-Aware Export**: Automatic chat title generation for intelligent file downloads.

## 🏗️ Architecture

The project follows a strict modular design pattern for maximum maintainability:

```text
OmniChat/
├── app.py             # Main entry point & state orchestration
├── modules/           # Core logic modules
│   ├── ai.py          # OpenAI engine & model mapping
│   ├── ui.py          # Components for sidebar & chat view
│   ├── css.py         # Advanced adaptive styling engine
│   ├── tools.py       # Token counting & utility functions
│   └── docs.py        # PDF & Text processing engine
├── .env               # Environment configuration (API Keys)
├── .gitignore         # Repository exclusions
└── requirements.txt   # Dependency management
```

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.9+ installed and an active OpenAI API Key.

### 2. Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_actual_key_here
```

### 4. Launch

Launch the application with Streamlit:

```bash
streamlit run app.py
```

## 🛠️ Tech Stack

- **Streamlit**: Application framework.
- **OpenAI API**: Large Language Model integration.
- **Python-Dotenv**: Configuration management.
- **PyPDF**: Document processing logic.
- **Vanilla CSS**: Advanced theme-aware UI refinements.

---
*Developed with a focus on aesthetics, modularity, and high-performance AI integration.*
