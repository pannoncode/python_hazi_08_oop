from utils.file_handler import read_file

from utils.class_file_hand import ReadDirectory, WriteFile
from utils.params import FolderPath

import re


def book_statistic():
    """
    legenerálja a fájlonkénti statisztikát (1. statisztika)
    """
    import math

    book_folder_path = FolderPath("books").folder
    stats_folder_path = FolderPath("stat_files").folder

    regTitle = r"Title: .*"
    regRelease = r"Release Date: .*"
    files = ReadDirectory(book_folder_path, "txt")
    books = read_file(book_folder_path, files.read)
    for idx in range(len(books)):
        releaseDate = re.findall(regRelease, books[idx])
        releaseDate = releaseDate[0][14:] if len(releaseDate) > 0 else ""
        title = re.findall(regTitle, books[idx])
        title = title[0][7:]
        stat_dict = {
            "releaseDate": releaseDate,
            "title": title,
            "pages": math.ceil(len(books[idx]) / 3000)
        }
        WriteFile(stats_folder_path, title, stat_dict)


def all_book_statistic():
    """
    összegyűjti a statisztikai adatokat és 
    kiíratja json fájlba
    """
    from utils.stat_data import collapse_data

    sing_stat_folder_path = FolderPath("single_stat_file").folder
    return WriteFile(sing_stat_folder_path, "statistics", collapse_data())


if __name__ == '__main__':
    book_statistic()
    all_book_statistic()
