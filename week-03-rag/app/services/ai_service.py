import openai
from app.core.config import settings
from app.services.embedding_service import query_documents

def chat_with_docs(question: str):

    openai_client = openai.OpenAI(api_key=settings.openai_api_key)

    results = query_documents(question)
    retrieved_chunks = results["documents"][0]  # list of relevant text chunks
    context = "\n".join(retrieved_chunks)

    response = openai_client.chat.completions.create(
        model=settings.model_name,
        messages=[
            {"role": "system",
             "content": f"You are a helpful assistant. Answer ONLY using the following context. If the answer isn't in the context, say you don't know.\n\nContext:\n{context}"},
            {"role": "user", "content": question}
        ]
    )

    # get the first choice
    message = response.choices[0].message
    return message.content
