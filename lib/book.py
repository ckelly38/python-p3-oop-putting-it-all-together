#!/usr/bin/env python3

class Book:
    def __init__(self, title, numpgs):
        self.title = title;
        self.set_page_count(numpgs);

    def get_page_count(self): return self._page_count;

    def set_page_count(self, val):
        #print(f"val = {val}");
        if (type(val) == int):
            print("in setter before changing the value!");
            self._page_count = val;
        else: print("page_count must be an integer");
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!");

    page_count = property(get_page_count, set_page_count);

#bk = Book("name", 10);
#bk.page_count = "str";
#print(f"bk.page_count = {bk.page_count}");
