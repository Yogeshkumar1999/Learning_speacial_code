import json


def convertList(array):
    if array is None:
        return []

    __array = []
    for item in array:
        if type(item) in [list]:
            __array.append(convertList(item))
        elif type(item) in [dict, JSONObject]:
            __array.append(item.convert())
        else:
            __array.append(item)
    return __array


class JSONObject:
    def __init__(self, dictionary):
        vars(self).update(dictionary)

    def keys(self):
        return self.__dict__.keys()

    @property
    def dictionary(self):
        return self.__dict__

    def convert(self):
        dictionary = {}
        for key in self.keys():
            if type(self.__dict__[key]) in [list]:
                dictionary[key] = convertList(self.__dict__[key])
            elif type(self.__dict__[key]) in [JSONObject]:
                dictionary[key] = self.__dict__[key].convert()
            else:
                dictionary[key] = self.__dict__[key]
        return dictionary

    def toJSON(self):
        return json.dumps(self.convert(),
                          ensure_ascii=True)


