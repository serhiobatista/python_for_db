class Counter:
    def __init__(self, curr_count=0):
        self.curr_count = 0

    def increment(self):
        self.curr_count += 1

    def decrement(self):
        if self.curr_count != 0:
            self.curr_count -= 1

    def get_counter(self):
        return self.curr_count

