from collections import deque


class QueueProcessing:
    def __init__(self):
        self.antrian = deque()

    def enqueue(self, mahasiswa):
        self.antrian.append(mahasiswa)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.antrian.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self.antrian[0]

    def is_empty(self):
        return len(self.antrian) == 0
