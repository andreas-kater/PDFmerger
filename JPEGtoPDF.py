from fpdf import FPDF
pdf = FPDF()
imagelist = [
'path/to/file/one.jpeg',
'path/to/file/two.jpeg',
        ]
# imagelist is the list with all image filenames
w = 248
h = 350
s = 0.75
w = w * s
h = h * s
for image in imagelist:
    pdf.add_page()
    pdf.image(image, w=w, h=h)
pdf.output("output.pdf", "F")
