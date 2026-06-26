import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import tempfile

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

st.title("📄 AI чатбот по документу")
st.write("Загрузи PDF и задавай вопросы по его содержимому")

uploaded_file = st.file_uploader("Загрузи PDF", type="pdf")

if uploaded_file:
    try:
        import pypdf
        reader = pypdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        
        if len(text.strip()) < 100:
            st.error("PDF содержит сканы, текст не читается. Загрузи другой файл.")
        else:
            st.success(f"Документ загружен! Страниц: {len(reader.pages)}, символов: {len(text)}")
        
        question = st.text_input("Задай вопрос по документу")
        if question:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Отвечай на вопросы только на основе этого документа:\n\n{text[:8000]}"},
                    {"role": "user", "content": question}
                ]
            )
            st.write("**Ответ:**", response.choices[0].message.content)
    except Exception as e:
        st.error(f"Ошибка: {e}")