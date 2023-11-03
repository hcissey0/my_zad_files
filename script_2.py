#!/usr/bin/python3

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
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


def script_2_main():
    folder_names = [i for i in sorted(os.listdir('.')) if os.path.isdir(i)]
    for folder in folder_names:
        print(f"[+] Working on '{folder}'")
        with change_dir(folder):
            file_names = [i for i in sorted(os.listdir('.')) if i.endswith('.pdf')]
            half = int(len(file_names) / 2)
            if len(file_names) % 2 != 0:
                half += 1
                pairs = list(zip(file_names[1:half], list(reversed(file_names))[:half]))
                pairs.insert(0, (file_names[0],))
            else:
                pairs = list(zip(file_names[:half], list(reversed(file_names))[:half]))
            for i, pair in enumerate(pairs, start=1):
                page = f'page_{i:02}'
                os.makedirs(page, exist_ok=True)
                for p in pair:
                    shutil.move(p, page)
                print(f"\t[-] Done with '{page}'")



if __name__ == "__main__":
    script_2_main()
    print("~~> Script_2 Done!!!")
