from fpdf import FPDF

name = input("Name: ")
pdf = FPDF(orientation = "portrait", unit = "mm", format = "A4")
pdf.add_page()
pdf.set_font('helvetica', 'B', 32)
pdf.cell(80, 40, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C", center=True)
pdf.set_auto_page_break(False)
pdf.image("/Users/jacoblaporte/Documents/Coding-Projects/shirtificate/shirtificate.png", x = 0, y = 60)
pdf.cell(80, 150, f"{name} took CS50", center=True, new_x="LMARGIN", new_y="NEXT", align="C")
pdf.output("shirtificate.pdf")