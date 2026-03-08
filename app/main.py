# import os
# from dotenv import load_dotenv
# import google.generativeai as genai
# from document_loader import load_pdf, chunk_text
# from vector_store import store_chunks, retrieve_similar
# from google import genai

# # Load API
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-pro")

# # Load PDF
# file_path = "data/sample.pdf"  # Put a PDF inside data folder
# text = load_pdf(file_path)

# chunks = chunk_text(text)
# store_chunks(chunks)

# # Ask question
# question = input("Ask a question: ")

# context_chunks = retrieve_similar(question)
# context = "\n".join(context_chunks)

# prompt = f"""
# Answer the question based only on the context below.

# Context:
# {context}

# Question:
# {question}
# """

# response = model.generate_content(prompt)

# print("\nAnswer:")
# print(response.text)

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# create client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# ask Gemini
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello in one short sentence."
)

print(response.text)