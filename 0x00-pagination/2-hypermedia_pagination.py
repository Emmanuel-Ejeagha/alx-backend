#!/usr/bin/env python3

"""Module that create a helper function"""

from typing import Tuple
import csv
import math
from typing import List, Mapping, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the pages using its index"""
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        s, e = index_range(page, page_size)
        data = self.dataset()
        data_f = data[s:e]
        length = len(data) - 1
        if e > length + 1 or s > length:
            return []
        return data_f

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str,
                                               Union[int, List[List], None]]:
        """Generate the hypermedia for the pages"""

        data = self.get_page(page=page, page_size=page_size)
        length = len(self.dataset())
        next_p = page + 1
        prev_p = page - 1
        total_pages = math.ceil(length / page_size)
        info = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_p if next_p <= total_pages else None,
            "prev_page": prev_p if prev_p > 0 else None,
            "total_pages": total_pages
            }
        return info


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Find the index range"""
    if page > -1:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
    return (start_index, end_index)
