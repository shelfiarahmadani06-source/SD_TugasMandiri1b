class StackUndo:
    def __init__(self):
        self.aktivitas = []

    def push(self, aktivitas):
        self.aktivitas.append(aktivitas)

    def pop(self):
        if self.is_empty():
            return None
        return self.aktivitas.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.aktivitas[-1]

    def is_empty(self):
        return len(self.aktivitas) == 0
