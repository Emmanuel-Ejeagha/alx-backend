#!/usr/bin/env python3

"""This module creates a basic cache class and
   inherit from a base cache class
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """use least recently use approach to caching"""

    def __init__(self):
        """Initialization method"""
        super().__init__()

    def put(self, key, item):
        """Put item into the cache implementing the
        LRU caching algorithm"""
        if key and item:
            self.cache_data.pop(key, None)
            self.cache_data[key] = item
            length = len(self.cache_data)
            if length > BaseCaching.MAX_ITEMS:
                key = list(self.cache_data)[0]
                del self.cache_data[key]
                print("DISCARD:", key)

    def get(self, key):
        """get the data"""
        if key:
            value = self.cache_data.get(key, None)
            if value:
                del self.cache_data[key]
                self.cache_data[key] = value
            return value
        return None
