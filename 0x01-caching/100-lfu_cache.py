#!/usr/bin/env python3
"""
Module containing the LFUCache class that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that inherits from BaseCaching.
    It has a size limit and uses the Least Frequently Used (LFU) algorithm
    to remove items when the limit is reached.
    If there is a tie in frequency, it uses Least Recently Used
    (LRU) to discard.
    """

    def __init__(self):
        """
        Initialize the class by calling the parent class initializer
        """
        super().__init__()
        self.frequency = {}  # Dictionary to track the frequency of each key
        self.usage_order = []  # List to track the order in which keys are used

    def put(self, key, item):
        """
        This method adds items to the cache using the LFU algorithm.
        If the cache exceeds the max limit, it discards the
        least frequently used item,
        and in case of a tie, the least recently used one is discarded.

        Args:
            key: key to the item to add
            item: item to add to the cache
        """
        if key is None or item is None:
            return

        # If key already exists, update the item and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If cache exceeds MAX_ITEMS, remove the least
            # frequently used or LRU item
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = self._get_lfu_key()
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print("DISCARD:", lfu_key)

            # Add the new key-value pair
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        This method gets items from the cache data using the key.
        If the key is accessed, its frequency is incremented.

        Args:
            key: key to the item to retrieve

        Returns:
            The item associated with the key, or None if the key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the usage and frequency when accessed
        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]

    def _get_lfu_key(self):
        """
        Helper method to find the least frequently used key.
        In case of a tie in frequency, the least recently used key is returned.

        Returns:
            The key to be discarded.
        """
        # Find the minimum frequency
        min_freq = min(self.frequency.values())
        # Get all keys with that frequency
        min_freq_keys = [key for key,
                         freq in self.frequency.items() if freq == min_freq]

        # If there's a tie, return the least recently used key
        for key in self.usage_order:
            if key in min_freq_keys:
                return key
