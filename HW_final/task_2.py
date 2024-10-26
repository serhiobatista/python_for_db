from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    @property
    def cache(self):
        return next(iter(self.cache_dict))

    @cache.setter
    def cache(self, key_value):
        key, value = key_value
        check = self.cache_dict.get(key, None)
        if check:
            self.cache_dict.move_to_end(key)
        self.cache_dict[key] = value

        if len(self.cache_dict) > self.capacity:
            self.cache_dict.popitem(last=False)

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")

    def get(self, key):
        res = self.cache_dict.get(key, None)
        if res:
            self.cache_dict.move_to_end(key)
            return res
        else:
            return -1
