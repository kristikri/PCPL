class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(items)

    def __next__(self):
        while True:
            try:
                item = next(self.iterator)
                key = item.lower() if self.ignore_case and isinstance(item, str) else item
                if key not in self.seen:
                    self.seen.add(key)
                    return item
            except StopIteration:
                raise StopIteration

    def __iter__(self):
        return self

if __name__ == "__main__":
    data = ['abc', 'def', 'ABC', 'ghi', 'DEF', 'jkl']
    unique_items = Unique(data, ignore_case=True)

    for item in unique_items:
        print(item)  