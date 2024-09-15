#!/usr/bin/env python3
"""Module for simple pagination"""

import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The number of the page.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of size two containing start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """
        Get a page with the given page number and page size

        Args:
            page (int, optional): The number of the page. Defaults to 1.
            page_size (int, optional): The number of items per page.
                Defaults to 10.

        Returns:
            List[List]: A list of the rows of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Method to get hypermedia pagination

        Args:
            page (int, optional): The number of the page. Defaults to 1.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            dict: A dictionary containing the following key-value pairs:
                - page_size: the length of the returned dataset page
                - page: the current page number
                - data: the dataset page (equivalent to return
                                          from previous task)
                - next_page: number of the next page, None if no next page
                - prev_page: number of the previous page, None if no
                                            previous page
                - total_pages: the total number of pages in the dataset as
                                                    an integer
        """

        data = self.data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) / page_size
        total_pages = int(total_pages) if total_pages.is_integer() else int(
            total_pages) + 1
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
