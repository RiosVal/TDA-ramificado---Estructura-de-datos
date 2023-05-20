import streamlit as st

def codeMonticulos():
    code = '''
    class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            return None
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_value
            self.heapify_down(0)
        return min_value

    def get_min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_index = index

            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] < self.heap[smallest_index]):
                smallest_index = left_child_index

            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] < self.heap[smallest_index]):
                smallest_index = right_child_index

            if smallest_index == index:
                break

            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            index = smallest_index
    '''
    st.code(code, language='python')


def codeMonticuloMax():
    code = '''
        import heapq

        class MaxHeap:
            def __init__(self):
                self.heap = []

            def insert(self, value):
                heapq.heappush(self.heap, -value)

            def extract_max(self):
                return -heapq.heappop(self.heap)

            def get_max(self):
                return -self.heap[0]

            def is_empty(self):
                return len(self.heap) == 0
        '''
    st.code(code, language='python')

def codeMonticuloMin():
    code = '''
        import heapq

        class MinHeap:
            def __init__(self):
                self.heap = []

            def insert(self, value):
                heapq.heappush(self.heap, value)

            def extract_min(self):
                return heapq.heappop(self.heap)

            def get_min(self):
                return self.heap[0]

            def is_empty(self):
                return len(self.heap) == 0
        '''
    st.code(code, language='python')