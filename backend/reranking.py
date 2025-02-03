from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from fastapi.responses import JSONResponse
from create_knowledge_base import get_vector_store
from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Helper function to format and print document content
def pretty_print_docs(docs):
    # Print each document in the list with a separator between them
    print(
        f"\n{'-' * 100}\n".join(  # Separator line for better readability
            [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]  # Format: Document number + content
        )
    )

reranking_router = APIRouter()
# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=os.environ.get("GOOGLE_API_KEY"))

# Models
class QueryRequest(BaseModel):
    question: str
    query_transformation_option:str

class QueryResponse(BaseModel):
    answer: str


@reranking_router.post("/response/")
async def generate_response(query: QueryRequest):

    vector_store = get_vector_store()
    if vector_store is None:
        return JSONResponse(content={"error": "Knowledge base not created. Please upload a PDF first."}, status_code=400)

    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    # Initialize the model
    model = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")

    # Select the top 3 documents
    compressor = CrossEncoderReranker(model=model, top_n=3)

    # Initialize the contextual compression retriever
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )

    # Retrieve compressed documents
    compressed_docs = compression_retriever.invoke(query.question)

    # Display the documents
    pretty_print_docs(compressed_docs)

    # Generate a response
    prompt_text = f"Question: {query.question}\n\nContext: {compressed_docs}\n\nAnswer:"
    response = llm.invoke(prompt_text)
    print(response)
    return  QueryResponse(answer=response.content)
    