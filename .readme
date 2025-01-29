# Policy Document Assistant

The **Policy Document Assistant** is an AI-powered application that helps employees or customers query company policies, compliance regulations, and HR handbooks with precision. It uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant policy sections and generate concise, user-friendly responses using a large language model (LLM).

---

## Features
- **Policy Querying**: Enables users to ask questions like "What is the company's leave policy?" or "How do I submit a reimbursement claim?".
- **Document Ingestion**: Automatically indexes policy documents (PDFs, DOCs, or plain text).
- **Accurate Retrieval**: Retrieves the most relevant sections of documents using vector embeddings.
- **Natural Language Responses**: Generates detailed yet simple explanations using an LLM.
- **Dynamic Document Updates**: Allows HR teams to add or update policy documents in real-time.
- **Dashboard**: Provides an intuitive user interface for queries and document management.

---

## Architecture
The application is built using the **RAG pipeline**:
![Architecture digram](images/RAG.png "Optional Tooltip")


1. **Document Ingestion**:
   - Policy documents are converted into text using OCR (for PDFs) or direct parsing (for text files).
   - Vector embeddings are created using a transformer-based model (e.g., Sentence Transformers) and stored in a vector database (e.g., Pinecone or FAISS).

2. **Query Processing**:
   - User queries are processed to generate embeddings.
   - The embeddings are matched against stored vectors to retrieve the most relevant sections.

3. **Response Generation**:
   - The retrieved sections are passed to an LLM (e.g., GPT-4) to generate a natural language response.

4. **Frontend**:
   - A React-based UI enables users to interact with the assistant and view results.
   - HR teams can upload and manage policy documents via a dashboard.

---

## Tech Stack
- **Backend**:
  - Python (FastAPI/Flask)
  - OpenAI GPT API (or Azure OpenAI)
  - Vector database: Pinecone, FAISS, or Weaviate
- **Frontend**:
  - React.js
  - Material-UI or Tailwind CSS for styling
- **Deployment**:
  - Docker for containerization
  - AWS/Azure/GCP for hosting
- **Additional Tools**:
  - Tesseract OCR (for PDF parsing)
  - Sentence Transformers (for embedding generation)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/policy-document-assistant.git
   cd policy-document-assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   npm install --prefix frontend
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the root directory and add the following:
   ```env
   OPENAI_API_KEY=<your_openai_api_key>
   VECTOR_DB_URL=<your_vector_database_url>
   ```

4. **Run the Application**:
   - Start the backend:
     ```bash
     python app.py
     ```
   - Start the frontend:
     ```bash
     npm start --prefix frontend
     ```

5. **Access the App**:
   Open your browser and navigate to `http://localhost:3000`.

---

## Usage

1. **Querying Policies**:
   - Enter your query in the search bar (e.g., "What is the leave policy?").
   - The assistant retrieves the most relevant sections and generates a response.

2. **Uploading Documents**:
   - HR teams can upload new policy documents or update existing ones via the dashboard.

3. **Viewing Results**:
   - Users can view the retrieved document sections alongside the AI-generated response for better transparency.

---

## Folder Structure
```
policy-document-assistant/
|
├── backend/               # Backend code (FastAPI/Flask)
│   ├── app.py            # Main application
│   ├── ingest.py         # Document ingestion logic
│   ├── retrieve.py       # Embedding retrieval logic
│   └── requirements.txt  # Python dependencies
|
├── frontend/              # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
|
├── docs/                  # Documentation and architecture diagrams
├── .env                   # Environment variables
└── README.md              # Project documentation
```

---

## Future Enhancements
- Add **multi-language support** to answer queries in different languages.
- Implement **role-based access control** for sensitive policy documents.
- Enhance retrieval with **semantic search** for better accuracy.
- Integrate with **Slack or Microsoft Teams** for quick policy queries.
- Provide **analytics dashboards** to track frequently asked questions.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push to the branch and submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For questions or collaboration, feel free to reach out:
- **Email**: minakshee.narayankar2000@gmail.com
- **GitHub**: [Minakshee25](https://github.com/Minakshee25)
