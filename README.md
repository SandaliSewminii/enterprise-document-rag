# Enterprise Document Q&A System (RAG)

An AI-powered system that allows users to ask questions about PDF documents using **Retrieval-Augmented Generation (RAG)**.
The system extracts text from PDF documents, converts the text into embeddings, stores them in a vector database, and retrieves relevant information to generate accurate answers using a large language model.

---

## Project Overview

Organizations often store important information in PDF files such as contracts, policies, reports, and documentation. Searching through these documents manually can be time-consuming.

This project provides an intelligent solution that enables users to ask natural language questions and receive answers based on the content of the document.

Example:

Question:
What is the contract expiration date?

Answer:
December 31, 2026

---
## Features

- PDF document ingestion
- Automatic text chunking
- Semantic search using embeddings
- Vector database storage with ChromaDB
- Retrieval-Augmented Generation pipeline
- Question answering using a large language model
- Command-line interface for user queries

---
## System Architecture

The system follows a **Retrieval-Augmented Generation (RAG)** pipeline.

1. Load PDF documents
2. Extract text from the document
3. Split text into manageable chunks
4. Generate embeddings using Sentence Transformers
5. Store embeddings in ChromaDB
6. Retrieve the most relevant chunks for a query
7. Use a language model to generate the final answer

This approach allows the system to answer questions using information directly from the document.

---
## Technologies Used

- Python
- ChromaDB (Vector Database)
- Sentence Transformers (Embeddings)
- Google Gemini API (LLM)
- PyPDF (PDF processing)
- NumPy
- Torch

---
## Project Structure

enterprise-document-rag
│
├── app
│ ├── main.py
│ ├── document_loader.py
│ ├── vector_store.py
│ ├── rag_pipeline.py
│ └── llm_handler.py
│
├── data
│ └── sample.pdf
│
├── utils
│ └── config.py
│
├── README.md
├── requirements.txt
└── .gitignore

---

## Example Workflow

1. Place your PDF document inside the `data` folder.
2. Run the program.
3. Ask questions related to the document.
4. The system retrieves relevant sections and generates an answer.

---

## Limitations

- Currently supports a single document at a time
- Command-line interface only
- Requires an API key for the language model

---
## Future Improvements

- Web-based user interface
- Support for multiple documents
- Chat-style conversation interface
- Highlighting source passages from documents
- Support for additional document formats

---

## Author

Sandali Sewmini

---

## License

This project is for educational and research purposes.

