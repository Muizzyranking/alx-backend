#!/usr/bin/env python3
"""
This module contains the index_range function
"""


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
