from django.test import TestCase
import json
# Create your tests here.
a={'error':'exit'}
b=json.dumps(a)
c=json.loads(b)
print(a,type(a))
print(b,type(b))
print(c,type(c))
