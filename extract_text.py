import pymupdf

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
        page_counter = f"[PAGE {page.number + 1}]\n"
        doc_text = page.get_textpage().extractText()
        text += page_counter + doc_text
    return text