# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:39:25 2020

@author: littl
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:58:45 2020

@author: littl
"""


def read_file(filename):
    lines = []
    with open(filename, "r", encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines): 
    person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == "貼圖":
                allen_sticker_count += 1
            elif s[2] == "圖片":
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == "貼圖":
                viki_sticker_count += 1
            elif s[2] == "圖片":
                viki_image_count += 1
            else: 
                for m in s[2:]:
                    viki_word_count += len(m)
    print("Allen said:", allen_word_count, "words")
    print("Allen sent:", allen_sticker_count, "sticker(s)")
    print("Allen sent:", allen_image_count, "image(s)")
    print("Viki said:", viki_word_count, "words")
    print("Viki sent:", viki_sticker_count, "sticker(s)")
    print("Viki sent:", viki_image_count, "image(s)")
        
        
def write_file(filename, lines):
    with open(filename, "w", encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines = read_file("LINE-Viki.txt")
    lines = convert(lines)
    # write_file("output.txt", lines)

main()





