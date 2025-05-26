import streamlit as st
import requests

#API_URL = st.secrets.get("API_URL") or "https://sql-chat-fastapi-demo.onrender.com"
API_URL = st.secrets.get("API_URL") or "https://groq-sql-agent-demo.onrender.com"
st.title("🧠 SQL 智能問答系統（Groq + LangChain + PostgreSQL）")

question = st.text_input("請輸入你的問題，例如：昨天的 API 請求數是多少？")

if st.button("查詢") and question:
    with st.spinner("查詢中..."):
        try:
            res = requests.post(
                f"{API_URL}/ask",
                json={"question": question},
                timeout=60
            )
            data = res.json()
            if "error" in data:
                st.error(f"查詢錯誤：{data['error']}")
            else:
                st.success("查詢成功！")
                st.write(data)
                st.write(data["result"])
        except Exception as e:
            st.error(f"發生錯誤：{e}")
