from utils.file_handler import read_file

from utils.class_file_hand import ReadDirectory
from utils.params import FolderPath

import re


def min_max_page(result_stats):
    """
    megkeresi az min max oldalszámot és visszaadja
    """
    all_pages = []
    page_statistics = []

    for item in result_stats:
        all_pages.append(item["pages"])
    max_page = max(all_pages)
    min_page = min(all_pages)

    for item in result_stats:
        if item["pages"] == max_page:
            longest_book = {
                "longest_book": {
                    "page_size": max_page,
                    "title": item["title"]
                }
            }
            page_statistics.append(longest_book)
        if item["pages"] == min_page:
            shortest_book = {
                "shortest_book": {
                    "page_size": min_page,
                    "title": item["title"]
                }
            }
            page_statistics.append(shortest_book)

    return page_statistics


def oldest_book(result_stats):
    """
    megkeresi a kiadás dátumát és visszaadja
    """

    rel_date_full = []
    reg_date = r"[0-9]{4}"
    for item in result_stats:
        rel_date_full.append(re.findall(reg_date, item["releaseDate"]))

    rel_date_min = []
    for dates in rel_date_full:
        if len(dates) > 0:
            rel_date_min.append(int(dates[0]))
    rel_date_min = min(rel_date_min)

    books = {}
    for items in result_stats:
        if len(re.findall(reg_date, items["releaseDate"])) > 0:
            if re.findall(reg_date, items["releaseDate"])[0] == str(rel_date_min):
                books.update({
                    f'oldest_book_{items["title"]}': {
                        "release_date": re.findall(reg_date, items["releaseDate"])[0],
                        "title": items["title"]
                    }
                })
    return books


def longest_title(result_stats):
    """
    megkeresi a leghosszabb könyv címet
    """
    title = []
    longest_title = []
    for item in result_stats:
        title.append(len(item["title"]))

    title_long = max(title)

    for item in result_stats:
        if len(item["title"]) == title_long:
            longest = {
                "title": item["title"],
                "length": title_long,
            }
            longest_title.append(longest)
    return longest_title


def more_than_five_character():
    """
    megkeresi, hogy melyik könyvben van a legtöbb 5 karakter vagy 
    annál hosszabb szavak
    """
    book_folder_path = FolderPath("books").folder
    regTitle = r"Title: .*"
    book = ReadDirectory(book_folder_path, "txt")
    books_result = read_file(book_folder_path, book.read)

    temp = []
    max_char_num = []
    book_title = []
    for idx in range(len(books_result)):
        for item in books_result[idx].split('\n'):
            temp.extend(item.split(' '))
        temp = [item.replace(",", "") for item in temp if len(item) >= 5]
        max_char_num.append(len(temp))
        book_title.append(re.findall(regTitle, books_result[idx])[0][7:])

    max_five_char_word = {}
    for idx, item in enumerate(max_char_num):
        if item == max(max_char_num):
            max_five_char_word = {
                "words_num":  max(max_char_num),
                "title": book_title[idx]
            }
    return max_five_char_word


def collapse_data():
    """
    Összesíti az adatokat
    """
    from utils.file_handler import convert_json_to_dict

    stats_folder_path = FolderPath("stat_files").folder

    files = ReadDirectory(stats_folder_path, "json")
    stats = read_file(stats_folder_path, files.read)
    result_stats = convert_json_to_dict(stats)

    result_statistics = {
        "longest_shortest_book": min_max_page(result_stats),
        "oldest_book": oldest_book(result_stats),
        "longest_title": longest_title(result_stats),
        "legtobb_5_karakteres_szo": more_than_five_character()
    }

    return result_statistics
