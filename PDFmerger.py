from PyPDF2 import PdfFileWriter, PdfFileReader
import os


class PDFmerger(object):
    def __init__(self):
        self.files = []
        self.output = PdfFileWriter()
        self.output_dir = 'output'
        self.BASEDIR = os.path.abspath(os.path.dirname(__file__))
        self.blank_page_filepath = os.path.join(self.BASEDIR, 'blank_page.pdf')
        self.input_directory = 'input'
        self.instructions_directory = 'instructions'
        self.output_file_name = 'result.pdf'
        self.add_blank_pages = False

    @staticmethod
    def get_num_pages(file_path):
        pdf = PdfFileReader(open(file_path, 'rb'))
        return pdf.getNumPages()

    def append_pdf(self, file_path):
        file = PdfFileReader(open(file_path, "rb"))
        [self.output.addPage(file.getPage(page_num)) for page_num in range(file.numPages)]

    def read_in_files_from_directory(self, directory):
        self.files = []
        for file in sorted(os.listdir(directory)):
            if '.pdf' in file:
                file_path = os.path.join(directory, file)
                self.files.append(file_path)
        self.files = sorted(self.files)

    def read_in_files_from_file(self, file_path):
        self.files = []
        with open(file_path, 'rb') as f:
            for file in f:
                # self.files.append(os.path.join(file_path, file.replace(b'\n', b'').decode('UTF-8')))
                self.files.append(os.path.join(self.input_directory, file.replace(b'\n', b'').decode('UTF-8')))

    def merge(self):
        if not self.files:
            print("No files to merge")
        for file_path in self.files:
            self.append_pdf(file_path)
            number_of_pages = self.get_num_pages(file_path)
            if number_of_pages % 2 != 0 and self.add_blank_pages:
                self.append_pdf(self.blank_page_filepath)
        self.output.write(open(os.path.join(self.output_dir,self.output_file_name), "wb"))

    def set_output_file_name(self, file_name):
        self.output_file_name = file_name.split('.pdf')[0] + '.pdf'

    def execute_instructions_files(self):
        # merges files in instructions file(s) in the order they're listed and
        # names merged file according to instruction file's name
        for instructions_file in sorted(os.listdir(self.instructions_directory)):
            self.files = []
            if '.txt' in instructions_file:
                with open(os.path.join(self.instructions_directory, instructions_file), 'r') as f:
                    for line in f.read().splitlines():
                        print(line)
                        self.files.append(os.path.join(self.input_directory,line))
                self.set_output_file_name(instructions_file.split('.')[0])
                self.merge()

if __name__ == '__main__':
    merger = PDFmerger()
    merger.execute_instructions_files()
