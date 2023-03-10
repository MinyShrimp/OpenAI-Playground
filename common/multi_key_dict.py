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

    def __check(self, keys: list, value: dict):
        """ 타입 체크
        """
        if type(keys) is not list or type(value) is not dict:
            raise TypeError("Not allowed 'key' or 'value' types.")

        mykeys = set(self.__KEYS.keys())
        if len(mykeys.intersection({*keys})) != 0:
            raise ValueError(f"Duplicated keys {keys}")

        return True

    def __add(self, keys: list[str], value: dict) -> tuple[list[str], dict]:
        """실제 추가를 위한 로직
        """
        self.__check(keys, value)

        uuid_str = uuid1()
        for key in keys:
            self.__KEYS[key] = uuid_str
        self.__VALUE[uuid_str] = value

        return keys, value

    def add(self, keys: list[str], value: dict) -> tuple[list[str], dict]:
        return self.__add(keys, value)

    def __get(self, key: str):
        if type(key) is not str:
            raise TypeError("Not allowed 'key' type. 'key' type is str.")
        if self.__KEYS.get(key) is None:
            return None
        return self.__VALUE[self.__KEYS[key]]

    def get(self, key: str):
        """ multi_dict.get("key")
        """
        return self.__get(key)

    def __getitem__(self, item: str):
        """ multi_dict["key"]
        """
        return self.__get(item)

    def keys(self):
        return self.__KEYS.keys()

    def values(self):
        return self.__VALUE.values()

    def items(self) -> list[tuple[list[str], dict]]:
        """ multi_dict.items()

        :return: [ [[K1, K2], V1], [[K3, K4], V2], ... ]
        """
        tmp_dict = {}
        for key, value in self.__KEYS.items():
            if tmp_dict.get(value) is None:
                tmp_dict[value] = [key]
            else:
                tmp_dict[value].append(key)

        return [(keys, self.__VALUE[value]) for value, keys in tmp_dict.items()]
