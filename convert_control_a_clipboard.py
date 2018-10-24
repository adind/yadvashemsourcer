"""
This file will convert the data taken when you control + a on a yadvashem data page and convert it easy copy and
pastable source material. It will also automatically copy it to your clipboard.

Author: Adin Drabkin <abd5264@rit.edu>
"""
#  MAKE SURE TO RUN install_pyperclip.bat PRIOR TO RUNNING
import pyperclip


def get_clipboard():
    data = []
    part = 0
    with open("conversion_cache.txt", "w+") as f:
        f.write(pyperclip.paste())
    with open("conversion_cache.txt", "r") as f:
        for line in f:
            line = line.strip()
            if part == 0:
                if line == "Submit Additions/Corrections":
                    part = 1
            elif part == 1:
                if line[:7] == "Item ID":
                    part = 2
                if part == 1:
                    data.append(line)
            elif part == 2:
                return data


def process(file):
    data = []
    for count, line in enumerate(file, start=1):  # solves bug of it having double new lines
        if count % 2 == 0:
            line = line.strip()
            length = len(line) - 1
            i = 0
            pt1 = ""
            pt2 = ""
            while i <= length:
                if line[i:i+1] != "\t":
                    pt1 += line[i]
                    i += 1
                else:
                    break
            pt2 = line[i + 1:]
            data.append(str(pt1) + ": " + str(pt2) + " |")
    return data


def convert_to_copy(data):
    data2 = "\r\n".join(data)
    pyperclip.copy(data2)


def main():
    convert_to_copy(process(get_clipboard()))
    open('conversion_cache.txt', 'w').close()  # clears cache

main()

