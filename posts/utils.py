import re
import datetime

from django.utils.html import strip_tags


def count_words(html_string):
    """Подсчет слов в html"""
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = count/161.0     # средняя скорость чтения на кириллице
    read_time_second = read_time_min*60
    read_time = str(datetime.timedelta(seconds=read_time_second))
    return read_time
