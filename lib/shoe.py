#!/usr/bin/env python3

class Shoe:
    def __init__(self, name, size):
        self.brand = name;
        self.setSize(size);
        self.conditon = "old";
    
    def setSize(self, val):
        if (type(val) == int): self._size = val;
        else: print("size must be an integer");
    
    def getSize(self): return self._size;

    size = property(getSize, setSize);

    def cobble(self):
        self.condition = "New";
        print("Your shoe is as good as new!");
