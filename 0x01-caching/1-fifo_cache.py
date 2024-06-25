#!/usr/bin/env python3
"""FIFO BaseCaching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Caching system
    '''

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''Add an item in the cache
        '''
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.queue[0]))
                del self.cache_data[self.queue[0]]
                del self.queue[0]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key
        '''
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
