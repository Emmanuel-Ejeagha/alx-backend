#!/usr/bin/env python3
"""This module creates a basic cache class
and inherit from a base cache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """The base caching system class"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def put(self, key, item):
        """assign to dictionary item"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value of key in cache_data"""
        if key:
            return self.cache_data.get(key, None)
        return None
