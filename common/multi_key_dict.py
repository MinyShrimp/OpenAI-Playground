from uuid import uuid1

'''
Since: 2023-03-08
Author: 김회민 ksk7584@gmail.com

MultiKey Dictionary

[K1, K2] => V1
[K3, K4] => V2
'''


class MultiKeyDict:
    __VALUE: dict = {}
    __KEYS: dict = {}

    def __del__(self):
        self.__VALUE.clear()
        self.__KEYS.clear()

    def __check(self, key: str, value: dict):
        if type(key) is not str or type(value) is not dict:
            raise TypeError("Not allowed 'key' or 'value' types.")

        if value.get("supports") is None:
            raise TypeError("MUST 'supports' key in 'value'. and 'supports' type is str array.")

        if len(set(self.__KEYS.keys()).intersection({key, *value["supports"]})) != 0:
            raise ValueError("Duplicated key and value['supports'].")

        return True

    def __add(self, key: str, value: dict):
        self.__check(key, value)

        uuid_str = uuid1()
        self.__KEYS[key] = uuid_str

        for sup in value.pop("supports"):
            self.__KEYS[sup] = uuid_str

        self.__VALUE[uuid_str] = value

    def add(self, key: str, value: dict):
        self.__add(key, value)

    def bulk_add(self, _dict: dict):
        for key, value in _dict.items():
            self.__add(key, value)

    def __get(self, key: str):
        if type(key) is not str:
            raise TypeError("Not allowed 'key' type. 'key' type is str.")
        if self.__KEYS.get(key) is None:
            return None
        return self.__VALUE[self.__KEYS[key]]

    def get(self, key: str):
        return self.__get(key)

    def __getitem__(self, item: str):
        return self.__get(item)

    def keys(self):
        return self.__KEYS.keys()

    def values(self):
        return self.__VALUE.values()

    def items(self):
        tmp_dict = {}
        for key, value in self.__KEYS.items():
            if tmp_dict.get(value) is None:
                tmp_dict[value] = [key]
            else:
                tmp_dict[value].append(key)

        return [(key, self.__VALUE[value]) for value, key in tmp_dict.items()]
