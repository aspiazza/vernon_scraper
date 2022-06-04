import pdfplumber


def vernon_ny_parser(pdf_file, search_param):
    """
    pdf_file: Specify PDF path
    search_param: Specify text to search for in property block
    """
    with pdfplumber.open(pdf_file) as pdf:
        with open(f"Vernon_{search_param}.txt", 'w') as txt_file:
            pdf_size = int(str(pdf.pages[-1])[6:-1]) - 1
            pdf_count = 0

            while pdf_count < pdf_size:
                page = pdf.pages[pdf_count]
                text = page.extract_text()
                property_block = text.split(
                    "**********************************************************************************************")

                for prop in property_block[2:-1]:

                    if f"{search_param}" in prop:
                        txt_file.write(prop)

                pdf_count = pdf_count + 1


vernon_ny_parser(pdf_file="2021_Final_Roll_Website_Updated.pdf", search_param="4 UNITS")
