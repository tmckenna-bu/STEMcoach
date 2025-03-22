import json
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

CHUNKS_PATH = "cleaned_curriculum_chunks.jsonl"
FAISS_INDEX_PATH = "faiss_index"

def load_documents(path):
    docs = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line)
            metadata = item['metadata']
            docs.append(Document(
                page_content=item['text'],
                metadata=metadata
            ))
    return docs

def main():
    print("📚 Loading curriculum documents...")
    documents = load_documents(CHUNKS_PATH)

    print("🧠 Generating embeddings with OpenAI...")
    embeddings = OpenAIEmbeddings()

    print("📦 Storing in FAISS index...")
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(FAISS_INDEX_PATH)

    print("✅ FAISS index created at:", FAISS_INDEX_PATH)

if __name__ == "__main__":
    main()
