# AI чатбот по документу / AI Document Chatbot

Веб-приложение для общения с PDF документами через AI.  
Web app for chatting with PDF documents using AI.

## Как работает / How it works
Загружаешь PDF → AI читает содержимое → задаёшь вопросы → получаешь ответы на основе документа.  
Upload PDF → AI reads the content → ask questions → get answers based on the document.

## Stack
- Python
- Streamlit
- Groq API (llama-3.3-70b-versatile)
- pypdf

## Установка / Setup
1. Клонируй репозиторий / Clone the repo
2. Установи зависимости / Install dependencies: `pip install -r requirements.txt`
3. Создай `.env` файл / Create `.env` file и добавь / and add: `GROQ_API_KEY=your_key`
4. Запусти / Run: `python -m streamlit run app.py`