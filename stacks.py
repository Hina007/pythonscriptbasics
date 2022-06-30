# #stack using list
# stack = []
#
# stack.insert(0, 1)
# print(stack)
# stack.insert(1,2)
# stack.pop(1)
# print(stack)
# stack.append(2)
# print(stack)

#stack using class and object

class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
    def pop(self):
        self.items.pop()

s = stack()

s.push(1)
print(s)