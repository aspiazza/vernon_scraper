import pdfplumber
import re
from icecream import ic


def vernon_ny_parser(pdf_file):
    """
    pdf_file: Specify PDF path
    units: Specify number of units
    """
    with pdfplumber.open(pdf_file) as pdf:
        pdf_size = int(str(pdf.pages[-1])[6:-1]) - 1
        pdf_count = 0

        while pdf_count < pdf_size:
            page = pdf.pages[pdf_count]
            text = page.extract_text()
            property_block = text.split(
                "**********************************************************************************************")

            for prop in property_block[2:-1]:
                prop = prop.replace("**********************", "")
                prop = re.split(r'\s{3,}', prop)

                ic(len(prop[:-1]))
                for i in prop[:-1]:
                    ic(i)
                exit()

            pdf_count = pdf_count + 1


vernon_ny_parser(pdf_file="2021_Final_Roll_Website_Updated.pdf")
