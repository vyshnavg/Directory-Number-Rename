# 08 - June - 2018

import glob, os, re

def str_to_raw(s):
    raw_map = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}
    return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)

def rename(dir, pattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        print(pathAndFilename)
        searchResult = re.search(r'\d+', pathAndFilename).group(0)
        print(searchResult)
        os.rename(pathAndFilename, 
                  os.path.join(dir, searchResult + " " + title + ext))

folderPath = input("Enter the Folder path : ")
extension = input("Enter the extension with *. (Example : *.mp4) : ")

folderPath = str_to_raw(folderPath)
extension = str_to_raw(extension)

rename(folderPath ,extension)


# def rename(dir, pattern, titlePattern):
#     for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
#         title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#         # os.rename(pathAndFilename, 
#         #           os.path.join(dir, titlePattern % title + ext))
#         print(pathAndFilename)
#         # for s in pathAndFilename.split() if s.isdigit():
#         #         print(s)
#         #         os.rename(pathAndFilename, 
#         #             os.path.join(dir, s % ext))
#         s = re.search(r'\d+', pathAndFilename).group(0)
#         print(s)
#         os.rename(pathAndFilename, 
#                   os.path.join(dir, s + ext))

# rename(r'C:\Users\', r'*.txt', r'new(%s)')
