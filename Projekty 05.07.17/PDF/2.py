# More pyFDPF snippets at https://pyfpdfbook.wordpress.com/
# Import FPDF class
from fpdf import FPDF

# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
pdf=FPDF(format='letter', unit='in')

# Add new page. Without this you cannot create the document.
pdf.add_page()

# Remember to always put one of these at least once.
pdf.set_font('Times','',10.0) 

column_width = 2.0
column_spacing = 0.15

# Here we save what will be the top of each columns
ybefore = pdf.get_y()

pdf.multi_cell(column_width, 0.15, "Mea tamquam constituto no, facete dissentiunt eos no. Eu agam delicata qui, ex mea utinam consetetur. Pro insolens vulputate id. Mea discere eligendi explicari eu, ut fugit soluta eum. Per wisi putant commodo at.")

# Notice we have to account for the left margin to get the spacing between 
# columns right.

pdf.set_xy(column_width + pdf.l_margin + column_spacing, ybefore) 

pdf.multi_cell(column_width, 0.15, "Vis at dolores ocurreret splendide. Noster dolorum repudiare vis ei, te augue summo vis. An vim quas torquatos, electram posidonium eam ea, eros blandit ea vel. Reque summo assueverit an sit. Sed nibh conceptam cu, pro in graeci ancillae constituto, eam eu oratio soleat instructior. No deleniti quaerendum vim, assum saepe munere ea vis, te tale tempor sit. An sed debet ocurreret adversarium, ne enim docendi mandamus sea.")

pdf.set_xy(2*(column_width + column_spacing) + pdf.l_margin, ybefore)

pdf.multi_cell(column_width, 0.15, "Lorem ipsum dolor sit amet, vel ne quando dissentias. Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. At mea wisi dolorum contentiones, in malis vitae viderer mel.")

pdf.output('multi_cell_3_cols.pdf','F')
