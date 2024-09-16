#!/usr/bin/env python3
"""
Module containing the MRUCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    LRUCache is a caching system that inherits from BaseCaching.
    It has a size limit and uses the Least Recently Used algorithm
    to remove items when the limit is reached.
    """

    def __init__(self):
        """ Initialize MRU caching """
        super().__init__()
        self.most_recent = ""

    def put(self, key, item):
        """
        This method adds items to the cache using the MRU algorithm.
        It removes the msot recently used item when the limit is reached.

        Args:
            key: key to the item to add
            item: item to add to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and\
                key not in self.cache_data:
            print("DISCARD:", self.most_recent)
            del self.cache_data[self.most_recent]
        self.cache_data[key] = item
        self.most_recent = key

    def get(self, key):
        """
        This method gets items from the cache data using the key.
        If the key is accessed, it becomes the most recently used.

        Args:
           key: key to the item to retrieve

        Returns:
           The item associated with the key, or None if the key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        self.most_recent = key
        return self.cache_data[key]
