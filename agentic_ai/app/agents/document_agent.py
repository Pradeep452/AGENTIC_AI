from app.tools.document_tool import gemini_document_qa
from app.tools.web_search_tool import web_search

def document_agent(question: str, document_text: str):
    answer = gemini_document_qa(document_text, question)

    if answer:
        return {
            "agent": "Document Intelligence Agent",
            "source": "Document",
            "answer": answer
        }

    return {
        "agent": "Web Intelligence Agent",
        "source": "Internet",
        "answer": web_search(question)
    }
