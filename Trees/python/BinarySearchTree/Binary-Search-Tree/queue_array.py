"""Python port of Queue.h - fixed capacity array based queue."""
from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def en_queue(self, e): ...   # adding an item to the queue

    @abstractmethod
    def de_queue(self): ...      # removing the front element

    @abstractmethod
    def is_empty(self): ...      # checking the queue for emptiness


class QueueOverflow(Exception):
    def __str__(self):
        return "Queue is full!"


class QueueUnderflow(Exception):
    def __str__(self):
        return "Queue is empty!"


class WrongQueueSize(Exception):
    def __str__(self):
        return "Wrong queue size_!"


class QueueArray(Queue):
    def __init__(self, size_):
        if size_ <= 0:
            raise WrongQueueSize()
        self.size_ = size_
        self.head_ = -1
        self.tail_ = -1
        self.queue_array_ = [None] * size_

    def en_queue(self, element):
        if self.head_ == -1:
            self.head_ = 0
        if self.tail_ == self.size_ - 1:
            raise QueueOverflow()
        self.tail_ += 1
        self.queue_array_[self.tail_] = element

    def de_queue(self):
        if self.is_empty():
            raise QueueUnderflow()
        item = self.queue_array_[self.head_]
        self.head_ += 1
        if self.head_ > self.tail_:
            self.head_ = self.tail_ = -1
        return item

    def is_empty(self):
        return self.head_ == -1 and self.tail_ == -1
