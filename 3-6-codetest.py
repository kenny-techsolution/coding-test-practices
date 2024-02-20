from collections import deque


class Animal():

  def __init__(self, name, type, order):
    self.type = type
    self.order = order
    self.name = name


class Dog(Animal):

  def __init__(self, name, order):
    super().__init__(name, "dog", order)


class Cat(Animal):

  def __init__(self, name, order):
    super().__init__(name, "cat", order)


class AnimalQueue:

  def __init__(self):
    self.dogs = deque()
    self.cats = deque()

  def enqueue(self, animal: Animal):
    if isinstance(animal, Dog):
      self.dogs.append(animal)
    elif isinstance(animal, Cat):
      self.cats.append(animal)

  def dequeue_any(self):
    if not self.dogs:
      return self.dequeue_cat()
    if not self.cats:
      return self.dequeue_dog()
    oldest_dog = self.dogs[0]
    oldest_cat = self.cats[0]
    if oldest_cat.order < oldest_dog.order:
      return self.cats.popleft()
    else:
      return self.dogs.popleft()

  def dequeue_dog(self):
    if self.dogs:
      self.dogs.popleft()

  def dequeue_cat(self):
    if self.cats:
      self.cats.popleft()
