from flask import Flask, render_template, request
from PyPDF2 import PdfWriter

app = Flask(__name__)

class PDFMerger:
    def __init__(self, pdf_list, new_name):
        self.pdf_list = pdf_list
        self.new_name = new_name

    def merge(self):
        merger = PdfWriter()
        for pdf in self.pdf_list:
            merger.append(pdf)

        merger.close()
        with open(self.new_name, "wb") as f:
            merger.write(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    pdf_list = request.form['pdf_list'].split()
    new_name = request.form['new_name']
    pdf_obj = PDFMerger(pdf_list=pdf_list, new_name=new_name)
    pdf_obj.merge()
    return 'PDF files merged successfully!'

if __name__ == '__main__':
    app.run(debug=True)


