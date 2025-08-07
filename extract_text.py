import re
import pymupdf

CDC_PATH = "documents/CDC_2025.pdf"

# range definied to get only relevant text
START_PAGE = 7
END_PAGE = 128


def extract_text_from_pdf(path: str, start: int, end: int) -> str:
    text = ""
    doc = pymupdf.open(path)
    total_pages = len(doc)

    start_page = max(start - 1, 0)
    end_page = min(end, total_pages)

    if start >= end:
        raise ValueError("Invalid range of pages.")

    for i in range(start_page, end_page):
        page = doc[i]
        doc_text = page.get_textpage().extractText()
        text += doc_text
    return text


def clean_text(txt: str) -> str:
    txt = "\n".join(
        line for line in txt.splitlines() if not re.fullmatch(r"\d+", line.strip())
    )
    txt = re.sub(r"\n\s\n", "\n", txt)
    return txt


def save_text_extracted(path: str) -> None:
    txt_extracted = extract_text_from_pdf(CDC_PATH, START_PAGE, END_PAGE)
    txt_cleaned = clean_text(txt_extracted)

    with open(path, "w", encoding="utf-8") as file:
        file.write(txt_cleaned)
