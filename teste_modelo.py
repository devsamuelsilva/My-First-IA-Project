from llama_cpp import Llama

# Carregar o modelo baixado
llm = Llama(model_path="C:/Users/samuel.silva/Documents/Energimp - Samuel/Projetos/IA-Projects/IA-Documents/models/mistral-small-24b-instruct-2501-q4_0.gguf")

# Fazer uma pergunta simples para testar
resposta = llm("O que é segurança da informação?")
print(resposta)
