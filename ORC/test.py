from PIL import Image
import pytesseract
from pathlib import Path

# Папка с фотками
IMAGE_FOLDER = "ORC/photos"

# Итоговый файл
OUTPUT_FILE = "lecture.txt"

# Поддерживаемые форматы
EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp"]

# Получаем список файлов
image_files = sorted(
    [
        f for f in Path(IMAGE_FOLDER).iterdir()
        if f.suffix.lower() in EXTENSIONS
    ]
)

full_text = ""

for image_path in image_files:
    print(f"Обработка: {image_path.name}")

    img = Image.open(image_path)

    # grayscale иногда улучшает OCR
    img = img.convert("L")

    text = pytesseract.image_to_string(
        img,
        lang="rus",
        config="--psm 6"
    )

    full_text += f"\n\n===== {image_path.name} =====\n\n"
    full_text += text

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"\nГотово -> {OUTPUT_FILE}")