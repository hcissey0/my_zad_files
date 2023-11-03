#!/usr/bin/python3

import os
import io
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from contextlib import contextmanager
import shutil


@contextmanager
def change_dir(folder):
    try:
        cwd = os.getcwd()
        os.chdir(folder)
        yield
    finally:
        os.chdir(cwd)

def script_3_main():
    mainfolders = [i for i in sorted(os.listdir('.')) if os.path.isdir(i)]
    for mainfolder in mainfolders:
        print(f"[+] Working on '{mainfolder}'")
        with change_dir(mainfolder):
            pagefolders = [i for i in sorted(os.listdir('.')) if os.path.isdir(i)]
            half = int(len(pagefolders) / 2)
            frontpages = pagefolders[::2]
            backpages = pagefolders[1::2]

            frontfolder = f'{mainfolder}_frontpages'
            backfolder = f'{mainfolder}_backpages'
            os.makedirs(frontfolder, exist_ok=True)
            os.makedirs(backfolder, exist_ok=True)
            for page in frontpages:
                shutil.move(page, frontfolder)
            print(f"\t[-] Done with '{frontfolder}'")
            for page in backpages:
                shutil.move(page, backfolder)
            print(f"\t[-] Done with '{backfolder}'")


if __name__ == "__main__":
    script_3_main()
    print("\n~~> Script_3 Done!!!")
