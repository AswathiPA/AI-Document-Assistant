import pymupdf
def extract_text_from_pdf(pdf_bytes):
    extracted_pages = []
    with pymupdf.open(
    stream=pdf_bytes, 
    filetype="pdf"
) as pdf_doument:

      page_count = len(pdf_doument)

      for page_number, page in enumerate(
        pdf_doument,start=1   
      ):
       page_text = page.get_text("text").strip()

       if page_text:
                extracted_pages.append(
                    f"--- Page {page_number} ---\n{page_text}"
                )

      full_text = "\n\n".join(extracted_pages)
    return full_text, page_count