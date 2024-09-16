#!/usr/bin/env python3
"""
Module containing the LIFOCache class that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching.
    It has a size limit and uses the Last In First Out algorithm
    to remove items when the limit is reached.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        This method adds items to the cache using FIFO algorithm
        it removes the first item entered into the cache when the
        limit is reached

        Args:
            key: key to the item to add
            item: item to add to the cache
        """
        discard_key = ""
        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_key = list(self.cache_data.keys())[-1]
            del self.cache_data[discard_key]
            print("DISCARD:", discard_key)

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        This method gets items from the cache data using the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
