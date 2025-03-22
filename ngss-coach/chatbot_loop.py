from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import openai
from intent_classifier import classify_intent

FAISS_INDEX_PATH = "faiss_index"
embeddings = OpenAIEmbeddings()
db = FAISS.load_local(FAISS_INDEX_PATH, embeddings)

base_system_prompt = """You are a warm, knowledgeable curriculum coach helping science teachers implement the NGSS.
Your tone is supportive, collaborative, and encouraging. Respond with practical suggestions and
classroom wisdom based on curriculum materials provided.
"""

def retrieve_chunks(query, k=3):
    return db.similarity_search(query, k=k)

def generate_response(user_query, intent, context_docs):
    context_text = "\n\n".join([f"Chunk {i+1}:\n{doc.page_content}" for i, doc in enumerate(context_docs)])
    
    prompt = base_system_prompt
    if intent == "identify_seps":
        prompt += "\nFocus on identifying science practices and how students engage in them."
    elif intent == "modeling_support":
        prompt += "\nFocus on where students build, revise, or use models."
    elif intent == "assessment_identification":
        prompt += "\nFocus on identifying embedded assessments and what standards they target."

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Teacher question: {user_query}\n\nCurriculum context:\n{context_text}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.6
    )

    return response['choices'][0]['message']['content']
