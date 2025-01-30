from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import LlamaCpp
from langchain.embeddings import HuggingFaceEmbeddings


# Wrapper para o SentenceTransformer
class SentenceTransformerEmbeddings:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        return self.model.encode(documents)

# Extrai o texto do documento
with open("documentos/NO 02 - Tempo Real.pdf", "r", encoding='latin1') as file:
    document_text = file.read()

# Divide o texto em partes menores
text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=50)
docs = text_splitter.split_text(document_text)

# Cria um banco de dados vetorial
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_texts(docs, embedding=embedding)

# Configura a IA para responder perguntas
qa_chain = RetrievalQA.from_chain_type(
    llm=LlamaCpp(model_path="models/mistral-small-24b-instruct-2501-q4_0.gguf"), 
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

def perguntar(pergunta):
    resposta = qa_chain.run(pergunta)
    return resposta

# Teste
print(perguntar("Após quanto tempo de falha de internet devo atuar?"))

