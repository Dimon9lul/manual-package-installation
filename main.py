import sys

sys.path.append("emptypackage.zip")  # Here you have to use your own path.

from emptypackage import base
from emptypackage.functional import input_functions, input_classes

print(base.func0())
print(base.func1())

new_object = input_classes.FunctionalClass("value")
print(new_object.value)

print(input_functions.infunc(55))