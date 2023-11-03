#!/usr/bin/python3

import os
import io
from PyPDF2 import PdfFileReader
from PIL import Image


def script_4_main():
    mainfolders = [
            i for i in sorted(os.listdir('.'))
            if os.path.isdir(i)
            ]

    for mainfolder in mainfolders:
        print(f"[+] Working with '{mainfolder}'")
        subfolders = [
                os.path.join(mainfolder, d) for d in sorted(os.listdir(mainfolder))
                if os.path.isdir(os.path.join(mainfolder, d))
                ]

        for subfolder in subfolders:
            print(f"\t[-] Working in '{subfolder}'")
            pagefolders = [
                    os.path.join(subfolder, p) for p in sorted(os.listdir(subfolder))
                    if os.path.isdir(os.path.join(subfolder, p))
                    ]

            for pagefolder in pagefolders:
                pdf_files = [
                        os.path.join(pagefolder, f) for f in sorted(os.listdir(pagefolder))
                        if f.endswith('.pdf')
                        ]
                if 'backpages' in subfolder:
                    pdf_files = list(reversed(pdf_files))

                images = []
                for file in pdf_files:
                    reader = PdfFileReader(file)
                    page = reader.getPage(0)
                    xObject = page['/Resources']['/XObject'].getObject()
                    for obj in xObject:
                        if xObject[obj]['/Subtype'] == '/Image':
                            try:
                                data = xObject[obj]._data
                                image = Image.open(io.BytesIO(data))
                                images.append(image)
                            except Exception as e:
                                print(f"Error convertin page to image: {file}\nError: ", e)

                if images:
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)

                    new_image = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for image in images:
                        new_image.paste(image, (x_offset, 0))
                        x_offset += image.width

                    new_image.save(os.path.join(pagefolder, 'merged.pdf'), "PDF")
                    print(f"\t\t[.] Done with '{pagefolder}/merged.pdf'")


if __name__ == "__main__":
    script_4_main()
    print("~~> Script_4 Done!!!")
