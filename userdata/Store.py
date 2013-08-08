import pickle, os
from os.path import expanduser

class Store:
    def __init__(self, filename='.r6_user_data'):
        self.__local_file__ = expanduser("~") + '/' + filename

        
    def __load_data__(self):
        try:
            with open(self.__local_file__, 'r') as existing:
                _data = pickle.load(existing)
                existing.close()
        except:
            _data = {}
        
        return _data
        
    def __get_local__(self, attribute):
        try:
            _data = self.__load_data__()
            out = _data[attribute]
        except:
            out = None
            
        return out
        
    def __store_data__(self, data):
        with open(self.__local_file__, 'w') as f:
            pickle.dump(data, f)
            f.close()

    def store(self, **kwargs):
        '''
        Locally caches values supplied
        '''
        _data = self.__load_data__()
        
        for key, value in kwargs.items():
            _data[key] = value
            
        self.__store_data__(_data)
        
    def remove_local(self):
        '''
        Removes the local cache file.  Typically used for testing cleanup
        '''
        try:
            os.unlink(self.__local_file__);
        except:
            pass
        
