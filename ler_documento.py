from unstructured.partition.pdf import partition_pdf

def extrair_texto_pdf(caminho_pdf):
    elementos = partition_pdf(filename=caminho_pdf)
    texto = "\n".join([elemento.text for elemento in elementos])
    return texto

# Teste com um documento PDF
texto = extrair_texto_pdf("documentos/ITOM EGP 01 Rev.00.pdf")
print(texto[:500])  # Exibir os primeiros 500 caracteres
