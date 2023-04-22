class Heap:
    def __init__(self, arr, children):
        self.arr = arr                              # Array representation of the heap
        self.children = children                    # Number of children per node
        for index, value in enumerate(self.arr):
            self.push(index, value)                 # Push each element into the heap

    def push(self, index, value):
        parent_index = (index - 1) // self.children                 # Find the parent index
        if parent_index >= 0 and self.arr[parent_index] < value:    # If the parent is smaller, swap
            self.arr[index] = self.arr[parent_index]                # push the parent down
            self.arr[parent_index] = value                          # push the value up
            self.push(parent_index, value)                          # recursively push the value up

    def remove_root(self):
        if self.arr:
            root_value = self.arr[0]                        # Save the root value
            last_index = len(self.arr) - 1                  # Find the last index
            self.arr[0] = self.arr[last_index]              # Move the last value to the root
            self.arr.pop()                                  # Remove the last value
            self.slide_down(curr_index = 0)                 # Slide the new root down until satisfied
            return root_value

    def slide_down(self, curr_index):
        while curr_index < len(self.arr):
            max_value = self.arr[curr_index]                                                            # Assume the current value is the max
            max_index = curr_index                                                                      # Assume the current index is the max
            for i in range(1, self.children+1):                                                         # Check each child
                child_index = self.children * curr_index + i                                            # Find the child index
                if child_index < len(self.arr) and self.arr[child_index] > max_value:                   # If the child is larger
                    max_value = self.arr[child_index]                                                   # Update the max value
                    max_index = child_index                                                             # Update the max index
            if max_index != curr_index:                                                                 # If the max index is not the current index
                self.arr[curr_index], self.arr[max_index] = self.arr[max_index], self.arr[curr_index]   # Swap the values
                curr_index = max_index                                                                  # Update the current index
            else:
                break                                                                                   # If the current index is the max index, stop (heap is satisfied)

    def print_heap(self, index=0, level=0):
        # Print the current node and its children recursively
        if index < len(self.arr):
            indent = " " * 4 * level
            print(f"{indent}{index}: {self.arr[index]}")
            for i in range(1, self.children+1):
                child_index = self.children * index + i
                self.print_heap(child_index, level+1)