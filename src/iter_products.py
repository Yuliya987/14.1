class IteratorProduct:
    """Итератор по товарам категории"""

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """Возвращает сам объект итератора"""
        return self

    def __next__(self):
        """Возвращает очередной товар категории"""
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        raise StopIteration
