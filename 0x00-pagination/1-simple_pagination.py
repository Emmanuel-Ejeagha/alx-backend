#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10."""

from typing import Tuple, List
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """he function should return a tuple of size two containing
        a start index and an end index corresponding to the range of indexes
        to return in a list for those particular pagination parameters."""
        if page > -1:
            start_index = (page - 1) * page_size
            end_index = start_index + page_size
            return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the pages using its index"""
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        s, e = self.index_range(page, page_size)
        data = self.dataset()
        data_f = data[s:e]
        length = len(data) - 1
        if e > length + 1 or s > length:
            return []
        return data_f

