#!/usr/bin/env python3

"""This module creates a basic cache class and
   inherit from a base cache class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """use least recently use approach to caching"""

    def __init__(self):
        """Initialization method"""
        super().__init__()
        self.counter = {}

    def put(self, key, item):
        """Put item into the cache implementing the
        LFU caching algorithm"""

        if key and item:
            # set the counter for the cache
            self.counter[key] = self.counter.get(key, 0) + 1

            # if key is present, pop it and send it to the back of the dict
            self.cache_data.pop(key, None)
            self.cache_data[key] = item

            length = len(self.cache_data)

            # if length is greater than the max number of items, do something
            if length > BaseCaching.MAX_ITEMS:
                key_small = list(self.cache_data)[0]
                value_small = self.counter[key_small]
                for key2, value2 in self.counter.items():
                    if value2 < value_small and key2 != key:
                        value_small = value2
                        key_small = key2

                del self.counter[key_small]
                del self.cache_data[key_small]
                print("DISCARD:", key_small)

    def get(self, key):
        """get the data"""
        if key:
            value = self.cache_data.get(key, None)
            if value:
                self.counter[key] = self.counter.setdefault(key, 0) + 1
                del self.cache_data[key]
                self.cache_data[key] = value
            return value
        return None
