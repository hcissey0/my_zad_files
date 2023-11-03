#!/usr/bin/python3

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def script_5_main():
    mainfolders = [
            i for i in sorted(os.listdir('.'))
            if os.path.isdir(i)
            ]

    for mainfolder in mainfolders:
        print(f"[+] Working with '{mainfolder}'")
        subfolders = [
                os.path.join(mainfolder, s) for s in sorted(os.listdir(mainfolder))
                if os.path.isdir(os.path.join(mainfolder, s))
                ]

        for subfolder in subfolders:
            pagefolders = [
                    os.path.join(subfolder, p) for p in sorted(os.listdir(subfolder))
                    if os.path.isdir(os.path.join(subfolder, p))
                    ]
            if 'backpages' in subfolder:
                pagefolders = list(reversed(pagefolders))

            pdf_writer = PdfFileWriter()

            for pagefolder in pagefolders:
                pdf_file = open(os.path.join(pagefolder, 'merged.pdf'), 'rb')
                pdf_reader = PdfFileReader(pdf_file)
                pdf_writer.addPage(pdf_reader.getPage(0))

            
            with open(f'{subfolder}.pdf', 'wb') as out_file:
                pdf_writer.write(out_file)
            print(f"\t[.] Done with '{subfolder}.pdf'")


if __name__ == "__main__":
    script_5_main()
    print("~~> Script_5 Done!!!")
