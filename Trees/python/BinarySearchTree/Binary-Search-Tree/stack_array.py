"""Python port of Stack.h - fixed capacity array based stack."""
from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def push(self, e): ...

    @abstractmethod
    def pop(self): ...

    @abstractmethod
    def is_empty(self): ...


class StackOverflow(Exception):
    def __str__(self):
        return "Stack overflow"


class StackUnderflow(Exception):
    def __str__(self):
        return "Stack underflow"


class WrongStackSize(Exception):
    def __str__(self):
        return "Wrong stack size_"


class StackArray(Stack):
    def __init__(self, s):
        if s <= 0:
            raise WrongStackSize()
        self.size_ = s
        self.top_ = -1
        self.arr_ = [None] * s

    def push(self, element):
        if self.top_ == self.size_ - 1:
            raise StackOverflow()
        self.top_ += 1
        self.arr_[self.top_] = element

    def pop(self):
        if self.top_ == -1:
            raise StackUnderflow()
        element = self.arr_[self.top_]
        self.top_ -= 1
        return element

    def is_empty(self):
        return self.top_ == -1

    def top(self):
        if self.is_empty():
            raise StackUnderflow()
        return self.arr_[self.top_]
