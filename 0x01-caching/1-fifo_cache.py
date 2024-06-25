#!/usr/bin/env python3
"""Small BaseCaching module
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
        lens = len(self.cache_data)
        if key not in self.cache_data and lens >= BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.queue[0]))
            del self.cache_data[self.queue[0]]
            del self.queue[0]
        else:
            pass
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key
        '''
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
