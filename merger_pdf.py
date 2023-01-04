from PyPDF2 import PdfMerger


merger = PdfMerger()

merger.append("chosen.pdf")
merger.append("Docs.pdf")

merger.write("merged.pdf")
merger.close()
