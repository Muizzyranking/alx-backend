#!/usr/bin/env pythono3
"""
Module containing the LRUCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system that inherits from BaseCaching.
    It has a size limit and uses the Least Recently Used algorithm
    to remove items when the limit is reached.
    """

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        This method adds items to the cache using the LRU algorithm.
        It removes the least recently used item when the limit is reached.

        Args:
            key: key to the item to add
            item: item to add to the cache
        """
        if key is not None and item is not None:
            # If the key is already in the cache, update the usage order
            if key in self.cache_data:
                self.usage_order.remove(key)
            # Add the key and item to the cache
            self.cache_data[key] = item
            self.usage_order.append(key)

            # If the cache exceeds the max limit,
            # remove the least recently used item
            if len(self.cache_data) > self.MAX_ITEMS:
                # Get and remove the least recently used key
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

    def get(self, key):
        """
        This method gets items from the cache data using the key.
        If the key is accessed, it becomes the most recently used.

        Args:
           key: key to the item to retrieve

        Returns:
           The item associated with the key, or None if the key doesn't exist
        """
        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
