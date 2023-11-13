
# 第三题： 分页助手    
 import math

class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    def item_count(self):
        return len(self.collection)
    
    def page_count(self):
        return math.ceil(self.item_count() / self.items_per_page)
    
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1: 
            
            last_page = self.item_count() % self.items_per_page
            return self.items_per_page if last_page == 0 else last_page
        else:
            return self.items_per_page
        
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count():
            return -1
        else:
            return item_index // self.items_per_page
