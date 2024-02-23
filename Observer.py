from abc import ABC, abstractmethod

# Subject interface
class Sender(ABC):

    def __init__(self):
        self._members = []

    def register(self, member):
        self._members.append(member)

    def unregister(self, member):
        self._members.remove(member)

    def notify(self, content):
        for member in self._members:
            member.update(content)
        
