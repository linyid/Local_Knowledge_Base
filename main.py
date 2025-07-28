from ingest import load_documents
from embed import embed_documents, save_vectorstore, load_vectorstore
from retrieve import retrieve_docs
from chat import ask_question
import json


def main():
    # Load base directories from config.json
    with open("config.json", "r") as f:
        config = json.load(f)
        base_dirs = config.get("include_dirs", [])

    docs = load_documents(base_dirs)
    vectordb = embed_documents(docs)
    save_vectorstore(vectordb)

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == 'exit':
            break
        top_docs = retrieve_docs(query, vectordb)
        response = ask_question(query, top_docs)
        print("\nAnswer:\n", response)


if __name__ == "__main__":
    main()
