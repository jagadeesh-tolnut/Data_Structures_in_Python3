class Dequeue:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0

    def display_first(self):
        if len(self.data)==0:
            pass
        else:
            return self.data[0]

    def display_last(self):
        if len(self.data) == 0:
            pass
        else:
            return self.data[-1]

    def add_first(self, element):
        self.data.insert(0,element)

    def add_last(self, element):
        self.data.append(element)

    def remove_first(self):
        if len(self.data) == 0:
            pass
        else:
            last_el=self.data.pop(0)
            return last_el

    def remove_last(self):
        if len(self.data) == 0:
            pass
        else:
            first_el=self.data.pop()
            return first_el

dq =Dequeue()
print(dq.is_empty())
dq.add_last(1)
dq.add_last(2)
dq.add_last(3)
dq.add_first(4)
print(dq.data)
dq.remove_last()
print(dq.data)
dq.remove_first()
print(dq.data)
print(dq.is_empty())

