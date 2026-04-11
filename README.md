# first-project
This is my first Git Repository.
<br>
Author - Rakesh (first git repo)

# Load a small text-generation model (google/flan-t5-small) and create a helper function
from transformers import pipeline

print("Loading model (this can take ~30 sec). Be patient...")
generator = pipeline("text2text-generation", model="google/flan-t5-small")
print("Model ready! You can now call generate_text(prompt).")

def generate_text(prompt):
    out = generator(prompt, max_length=120)
    return out[0]['generated_text']
    
# Try simple prompts — edit the text inside the quotes
prompt = "Summarize this in one sentence: Machine learning helps computers learn from data."
result = generate_text(prompt)
print("Prompt:", prompt)
print("\nModel says:\n", result)












import yfinance as yf
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="5d").to_string()

def build_rag():
    loader = TextLoader("data.txt")
    docs = loader.load()
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma.from_documents(docs, embeddings)
    return db

def ask_ai(db, question, stock_data):
    llm = Ollama(model="Reebo")
    docs = db.similarity_search(question)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are an Indian stock market expert.

Context:
{context}

Stock Data:
{stock_data}

Question:
{question}

Give:
- Trend
- Risk
- Final decision: Buy, Sell, or Hold
"""

    return llm.invoke(prompt)

def main():
    db = build_rag()
    symbol = input("Enter stock symbol like RELIANCE.NS: ")
    question = input("Ask your question: ")
    stock_data = get_stock_data(symbol)
    answer = ask_ai(db, question, stock_data)
    print("\nAI Answer:\n")
    print(answer)

if __name__ == "__main__":
    main()
