__author__ = 'Sean'
import copy

class Foo:
    notagoodidea = 'what am I now?'

object1 = Foo()
object1.notagoodidea = 'who knows.'

object2 = object1
object2.notagoodidea = "Who's on first?"

print(Foo.notagoodidea)
print(object1.notagoodidea)
print(object2.notagoodidea)

object3 = copy.copy(object1)
object3.notagoodidea = "I'm Lost!"

print(Foo.notagoodidea, id(Foo.notagoodidea), id(Foo))
print(object1.notagoodidea, id(object1.notagoodidea), id(object1))
print(object2.notagoodidea, id(object2.notagoodidea), id(object2))
print(object3.notagoodidea, id(object3.notagoodidea), id(object3))