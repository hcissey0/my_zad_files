#!/usr/bin/python3
"""This script takes pdf files in a folder and splits them into pages"""

import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def script_1_main():
    file_names = get_file_names()
    folder_names = get_folder_names()

    for i, file in enumerate(file_names):
        pdf_file = open(file, 'rb')
        pdf_reader = PdfFileReader(pdf_file)

        os.makedirs(f"{folder_names[i]}", exist_ok=True)
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page_num))

            outfile = f'{folder_names[i]}/{folder_names[i]}_{page_num+1:03}.pdf'
            with open(outfile, 'wb') as out_pdf:
                pdf_writer.write(out_pdf)

        print(f"[+] Done with '{folder_names[i]}'")
        pdf_file.close()


def get_file_names():
    return [i for i in sorted(os.listdir('.')) if i.endswith('.pdf')]


def get_folder_names():
    ret = []
    for i in sorted(os.listdir('.')):
        if i.endswith('.pdf'):
            i = i[21:-4].lower()
            if i.startswith('al'):
                i = i[2:]
            ret.append(i)
    return ret


if __name__ == "__main__":
    script_1_main()

    print("\n~~> Script_1 Done!!!\n")
