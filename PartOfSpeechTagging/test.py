from collections import defaultdict
import math
import sys


def print_dict(dict_to_print):
    for key, val in dict_to_print.iteritems():
        print 'Key ->', key, 'Val ->', val


def normalize_dict1(dict_to_normalize):
    total_log = math.log(sum(dict_to_normalize.values()))
    for key, val in dict_to_normalize.iteritems():
        dict_to_normalize[key] = total_log - math.log(val)


def normalize_dict2(dict_to_normalize):
    total = sum(dict_to_normalize.values())
    for key, val in dict_to_normalize.iteritems():
        dict_to_normalize[key] = - math.log((0.0 + val) / total)


sys.stdout = open('output.txt', 'w')
print 'Hello World'
def_dict = defaultdict(dict)
def_dict['a'][1] = 2
def_dict['a'][2] = 4
def_dict['a'][3] = 8
def_dict['a'][4] = 16
def_dict['a'][5] = 32

print_dict(def_dict['a'])
normalize_dict2(def_dict['a'])
print_dict(def_dict['a'])

myint = 12
print sys.getsizeof(myint)

mychar = 'a'
print sys.getsizeof(mychar)


print sys.float_info.max
