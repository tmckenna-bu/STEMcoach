import streamlit as st
from chatbot_loop import retrieve_chunks, generate_response
from intent_classifier import classify_intent

st.set_page_config(page_title="STEM EquityCoach", layout="wide")

st.title("👩‍🏫 STEM EquityCoach")
st.markdown("Your NGSS-aligned, curriculum-smart, teacher-supportive chatbot coach.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask your coach a question:", "")

if query:
    st.session_state.chat_history.append(("user", query))

    intent = classify_intent(query)
    docs = retrieve_chunks(query)
    coach_reply = generate_response(query, intent, docs)

    st.session_state.chat_history.append(("coach", coach_reply))

for speaker, text in st.session_state.chat_history:
    if speaker == "user":
        st.markdown(f"**🧑‍🏫 You:** {text}")
    else:
        st.markdown(f"**🤖 Coach:** {text}")
