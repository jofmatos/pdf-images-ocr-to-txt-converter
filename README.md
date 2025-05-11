# PDF OCR Extractor

Converte PDFs (texto + imagens) em um TXT via OCR (Tesseract).

## Pré-requisitos

- Docker instalado  
- (Opcional) Tesseract local, para testes fora do container  

## Como usar

1. Abra um terminal (PowerShell, Terminal no macOS/Linux).

# 1. Clone
```bash
git clone https://github.com/jofmatos/pdf-OCR-extractor.git
cd pdf-OCR-extractor
```

# 2. Build da imagem

3. (Opcional) Verifique se o Docker está funcionando:

   ```bash
   docker --version
   ```
4. Faça o build da imagem Docker (só precisa rodar uma vez):

   ```bash
   docker build -t pdf-ocr-extractor .
   ```

   Isso criará a imagem chamada **pdf-ocr-extractor** localmente.

---

# 3. Rodar o container
#    monta a pasta atual em /app e processa o PDF

   * **Linux/macOS**

     ```bash
     docker run --rm \
       -v "$(pwd)":/app \
       pdf-ocr-extractor \
       seu_arquivo.pdf
     ```

   * **PowerShell (Windows)**

     ```powershell
     docker run --rm `
       -v ${PWD}.Path:/app `
       pdf-ocr-extractor `
       seu_arquivo.pdf
     ```

# Saída: seu_pdf_ocr.txt na pasta atual

```

---

## Pré-requisitos

* **Docker** instalado e em execução.

  * Windows: use o instalador em [https://docs.docker.com/desktop/install/windows/](https://docs.docker.com/desktop/install/windows/)
  * macOS: use [https://docs.docker.com/desktop/install/mac/](https://docs.docker.com/desktop/install/mac/)
  * Linux: siga [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
* (Opcional, para uso local) **Python 3.7+**, **Tesseract OCR** e dependências Python.

---

## Estrutura do repositório

```
pdf-ocr-extractor/
├── Dockerfile
├── .dockerignore
├── extract_pdf.py
├── requirements.txt
└── README.md
```

---

## Configuração do Docker


   ```
3. (Opcional) Verifique se o Docker está funcionando:

   ```bash
   docker --version
   ```
4. Faça o build da imagem Docker (só precisa rodar uma vez):

   ```bash
   docker build -t pdf-ocr-extractor .
   ```

   Isso criará a imagem chamada **pdf-ocr-extractor** localmente.

---

## Uso com Docker

1. Coloque o PDF que deseja processar dentro da pasta do projeto ou em qualquer pasta de sua preferência.

2. Execute o container montando a pasta onde o PDF está para dentro do container:

   * **Linux/macOS**

     ```bash
     docker run --rm \
       -v "$(pwd)":/app \
       pdf-ocr-extractor \
       seu_arquivo.pdf
     ```

   * **PowerShell (Windows)**

     ```powershell
     docker run --rm `
       -v ${PWD}.Path:/app `
       pdf-ocr-extractor `
       seu_arquivo.pdf
     ```

3. O script processará o PDF (`extract_pdf.py`) e gerará um arquivo de saída com o sufixo `_ocr.txt`, por exemplo, `seu_arquivo_ocr.txt`, na mesma pasta do host.

---

## Exemplos

* PDF de entrada: `relatorio.pdf`
* Comando:

  ```bash
  docker run --rm -v "$(pwd)":/app pdf-ocr-extractor relatorio.pdf
  ```
* Saída gerada: `relatorio_ocr.txt`

---

## Uso local (sem Docker)

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .\.venv\Scripts\Activate.ps1  # PowerShell
   ```
2. Instale dependências:

   ```bash
   pip install -r requirements.txt
   ```
3. Execute:

   ```bash
   python extract_pdf.py seu_arquivo.pdf
   ```

---

## Personalizações e Troubleshooting

* Para mudar o idioma do OCR, instale outro pacote no Dockerfile (ex.: `tesseract-ocr-eng`) e ajuste `lang="eng"` em `extract_pdf.py`.
* Se receber erro de permissão ou volume inválido no Windows, use `${PWD}.Path` no PowerShell ou forneça o caminho absoluto.
* Para inspecionar o conteúdo montado, abra um shell no container:

  ```bash
  docker run --rm -it -v "$(pwd)":/data pdf-ocr-extractor bash
  ls /data
  ```

---

## Licença

MIT
