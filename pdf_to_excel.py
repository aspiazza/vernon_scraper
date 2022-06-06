import pdfplumber
import re
from openpyxl import Workbook


# Work in progress
def vernon_ny_parser(pdf_file):
    """
    pdf_file: Specify PDF path
    """
    pdf_count = 0
    row = 2
    wb = Workbook()
    ws = wb.active

    column_list = ["Property Address", "Account Number", "Tax Map Parcel ID", "Apartment",
                   "Current Owners Name", "Current Owners Address", "Number of Units"]
    ws.append(column_list)

    with pdfplumber.open(pdf_file) as pdf:
        pdf_size = int(str(pdf.pages[-1])[6:-1]) - 1

        while pdf_count < pdf_size:
            page = pdf.pages[pdf_count]
            text = page.extract_text()
            property_blocks = text.split(
                "**********************************************************************************************")

            for property_block in property_blocks[1:-1]:
                property_block = property_block.replace("**********************", "")
                property_block = re.split(r'\s{4,}', property_block)

                for index, text_line in enumerate(property_block[1:]):
                    if index == 4 or index == 5 or index == 7 or index == 8 or index == 9:
                        continue
                    elif index == 0:
                        cell_ref = ws.cell(row=row, column=1)
                        cell_ref.value = text_line
                    elif index == 1:
                        cell_ref = ws.cell(row=row, column=2)
                        cell_ref.value = text_line
                    elif index == 2:
                        cell_ref = ws.cell(row=row, column=3)
                        cell_ref.value = text_line
                    elif index == 3:
                        cell_ref = ws.cell(row=row, column=4)
                        cell_ref.value = text_line
                    elif index == 6:
                        cell_ref = ws.cell(row=row, column=5)
                        cell_ref.value = text_line
                    elif index == 10:
                        cell_ref = ws.cell(row=row, column=6)
                        cell_ref.value = text_line
                    elif "UNITS" in text_line:
                        cell_ref = ws.cell(row=row, column=7)
                        cell_ref.value = text_line
                    else:
                        continue
                row += 1

            pdf_count = pdf_count + 1

    wb.save("vernon_real_estate_2021.xlsx")
    pdf.close()


vernon_ny_parser(pdf_file="2021_Final_Roll_Website_Updated.pdf")
