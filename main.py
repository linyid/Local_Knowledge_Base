from ingest import load_documents
import json


def main():
    collected_docs = load_documents()
    print(collected_docs)
    print(f"Collected {len(collected_docs)} documents.")




if __name__ == "__main__":
    main()
    
