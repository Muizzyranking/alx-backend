#!/usr/bin/env python3
"""
Module containing the BasicCache class that inherits from BaseCaching
BasicCache has no size limit and allows for storing and retrieving items
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class definition
    """

    def put(self, key, item):
        """
        Method to add items into the cache

        Args:
            key: key to the item to add
            item: item to add to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Method to get items from the cache data

        Args:
            key: key to the item to get

        Returns:
            Value in self.cache_data linked to key or None if key not found
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
