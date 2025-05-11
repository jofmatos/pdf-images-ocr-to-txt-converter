# 1. Imagem base leve com Python 3.13
FROM python:3.13-slim

# 2. Instala Tesseract + idioma pt + poppler para PDFs
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      tesseract-ocr \
      tesseract-ocr-por \
      poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. Copia dependências e instala
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o script
COPY extract_pdf.py ./

# 5. Entrypoint e argumento padrão
ENTRYPOINT ["python", "extract_pdf.py"]
CMD ["entrada.pdf"]