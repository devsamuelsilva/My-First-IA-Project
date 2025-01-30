from llama_cpp import Llama

# Carregar o modelo baixado
llm = Llama(model_path="models/mistral-7b-q4.gguf")

# Fazer uma pergunta simples para testar
resposta = llm("O que é segurança da informação?")
print(resposta)
