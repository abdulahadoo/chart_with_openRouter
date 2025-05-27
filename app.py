import streamlit as st
from openai import OpenAI

# ✅ Configure the OpenAI client for OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # 🔑 Replace with your actual key
    default_headers={
        "HTTP-Referer": "https://yourproject.com",  # Optional
        "X-Title": "My OpenRouter App"              # Optional
    }
)

# ✅ Streamlit App
st.set_page_config(page_title="Chat with OpenRouter")
st.title("🤖 Chat with OpenRouter")

user_prompt = st.text_input("Ask something:")

if user_prompt:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",  # Free model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ]
        )
        st.markdown("### 🔍 Response:")
        st.write(response.choices[0].message.content)
