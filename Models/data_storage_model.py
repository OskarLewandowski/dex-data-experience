class DataStorageModel:
    _dataFrames = {}

    @classmethod
    def add(cls, key, data_frame):
        original_key = key
        i = 1
        while cls.is_exists(key):
            key = f"{original_key}{i}"
            i += 1

        cls._dataFrames[key] = data_frame

    @classmethod
    def get(cls, key):
        return cls._dataFrames.get(key, None)

    @classmethod
    def update(cls, key, new_data_frame):
        if key in cls._dataFrames:
            cls._dataFrames[key] = new_data_frame
            return True
        else:
            return False

    @classmethod
    def remove(cls, key):
        if key in cls._dataFrames:
            del cls._dataFrames[key]
            return True
        else:
            return False

    @classmethod
    def get_all_keys(cls):
        return list(cls._dataFrames.keys())

    @classmethod
    def is_exists(cls, key):
        if key in cls._dataFrames:
            return True
        else:
            return False

    @classmethod
    def copy(cls):
        return cls._dataFrames.copy()

    @classmethod
    def clear(cls):
        cls._dataFrames.clear()

    @classmethod
    def get_all_keys_and_columns(cls):
        result = []
        for key, data_frame in cls._dataFrames.items():
            columns = data_frame.columns
            for column in columns:
                result.append(f"{key} : {column}")
        return result

    @classmethod
    def rename_key(cls, old_key, new_key):
        if not cls.is_exists(new_key):
            if old_key in cls._dataFrames:
                data_frame = cls._dataFrames.pop(old_key)
                cls._dataFrames[new_key] = data_frame
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def get_data_by_key_and_column(cls, key, column):
        if key in cls._dataFrames:
            data_frame = cls._dataFrames[key]
            if column in data_frame.columns:
                return data_frame[column]
        return None
