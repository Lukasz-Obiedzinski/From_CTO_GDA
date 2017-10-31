from fpdf import FPDF

pdf = FPDF()
# compression is not yet supported in py3k version
pdf.compress = True
pdf.add_page()
pdf.set_font('Arial', 'i', 14)  
pdf.ln(10)
pdf.write(5, 'hello world áéíóúüñ')
pdf.output('py3k.pdf', 'F')
