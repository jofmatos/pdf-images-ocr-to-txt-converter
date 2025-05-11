import sys
import fitz
import io
from PIL import Image
import pytesseract
from tqdm import tqdm

# PDF de entrada e saída
PDF = sys.argv[1] if len(sys.argv) > 1 else "entrada.pdf"
OUT = f"{PDF.rsplit('.', 1)[0]}_ocr.txt"

# (opcional) se o tesseract não estiver no PATH, descomente e ajuste:
# pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

doc = fitz.open(PDF)
with open(OUT, "w", encoding="utf-8") as out, tqdm(total=len(doc), ncols=70) as bar:
    for i, page in enumerate(doc, start=1):
        bar.set_description(f"Pág. {i}/{len(doc)}")
        text = page.get_text("text").strip()
        if text:
            out.write(f"\n\n--- Página {i} (texto) ---\n{text}\n")
        for j, img_info in enumerate(page.get_images(full=True), start=1):
            xref = img_info[0]
            base = doc.extract_image(xref)
            img = Image.open(io.BytesIO(base["image"]))
            try:
                ocr = pytesseract.image_to_string(img, lang="por")
            except:
                ocr = pytesseract.image_to_string(img)
            if ocr.strip():
                out.write(f"\n\n--- Página {i} | Imagem {j} ---\n{ocr}\n")
        bar.update(1)
print("Concluído. Saída em", OUT)
