# PDF OCR Extractor

Converte PDFs (texto + imagens) em um TXT via OCR (Tesseract).

## Pré-requisitos

- Docker instalado  
- (Opcional) Tesseract local, para testes fora do container  

## Como usar

```bash
# 1. Clone
git clone https://github.com/<seu-usuário>/pdf-ocr-extractor.git
cd pdf-ocr-extractor

# 2. Build da imagem
docker build -t pdf-ocr-extractor .

# 3. Rodar o container
#    monta a pasta atual em /app e processa o PDF
docker run --rm \
  -v "$(pwd)":/app \
  pdf-ocr-extractor \
  seu_documento.pdf

# Saída: seu_documento_ocr.txt na pasta atual