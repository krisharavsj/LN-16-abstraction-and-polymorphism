from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,f):
        print("passed value", f)
    @abstractmethod
    def task(self):
        print("we are inside Absclass")
class subclass(Absclass):
    def task(self):
        print("we are now inside subclass")
subobject=subclass()
subobject.task()
subobject.print(36)