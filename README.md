# 🦙 Enhanced Q&A Chatbot with Ollama

This is an **open-source Q&A Chatbot** built with **Streamlit** and **Ollama LLMs**, using **LangChain** for prompt management and response parsing. Ask questions and get answers powered by local LLM models like `phi3` and `gemma2`.

---

## ⚡ Features

- Interactive chat interface with **Streamlit**.
- Choose between **open-source Ollama models**: `phi3`, `gemma2`.
- Adjust **temperature** for creativity and **max tokens** for response length.
- Stores **chat history** during the session.
- Clear chat button to reset conversation.
- Simple and clean UI for easy use.

---

## ⚠️ Deployment Note

> This app **cannot be deployed on Streamlit Cloud** because Ollama requires a **local server running on your machine**.  

You need to:

1. Install [Ollama](https://ollama.com/).  
2. Run your Ollama server locally:  
   ```bash
   ollama serve

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM Framework:** LangChain  
- **Models:** Ollama open-source models (phi3, gemma2)  
- **Language:** Python  

---
## 📁 Project Structure
- ├── app.py # Main Streamlit application
- ├── requirements.txt # Python dependencies
- ├── README.md # Project documentation
- ├── runtime.tx
---

## ⚙️ Installation & Setup (Local)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ollama-qna-chatbot.git
cd ollama-qna-chatbot


