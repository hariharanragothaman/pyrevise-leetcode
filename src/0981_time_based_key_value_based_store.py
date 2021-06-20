from collections import defaultdict
from bisect import bisect_left


class TimeMap:
    def __init__(self):
        self.data_structure = defaultdict(list)

    def set(self, key, value, timestamp) -> None:
        self.data_structure[key].append((timestamp, value))

    def get(self, key, timestamp) -> str:
        if key in self.data_structure:
            _tmp = self.data_structure[key]
            times = [c[0] for c in _tmp]
            index = bisect_left(times, timestamp)
            if index != len(times) and times[index] == timestamp:
                return _tmp[index][1]
            else:
                if index - 1 >= 0:
                    return _tmp[index - 1][1]
                else:
                    return ""
        else:
            return ""


if __name__ == "__main__":
    obj = TimeMap()

    obj.set("love", "high", 10)
    obj.set("love", "low", 20)

    res = obj.get("love", 5)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 10)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 15)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 20)
    print(f"The result is: {res}")
    print("*" * 10)

    res = obj.get("love", 25)
    print(f"The result is: {res}")
    print("*" * 10)

    # obj.set("foo", "bar2", 4)
    #
    # res = obj.get("foo", 4)
    # print(f"The result is: {res}")
    # print("*"*10)
    #
    # res = obj.get("foo", 5)
    # print(f"The result is: {res}")
    # print("*"*10)