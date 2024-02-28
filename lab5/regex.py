#1
import re

def m(s):
    p = r'ab*'
    if re.match(p, s):
        return True
    else:
        return False

t = ['a', 'ab', 'abb', 'aac']

for s in t:
    print(f"{s}: {m(s)}")

#2
import re

def m(s):
    p = r'ab{2,3}'
    if re.match(p, s):
        return True
    else:
        return False

t = ['a', 'ab', 'abb', 'abbb', 'abbbb']

for s in t:
    print(f"{s}: {m(s)}")

#3
import re

def f(s):
    p = r'[a-z]+_[a-z]+'
    m = re.findall(p, s)
    return m

i = "example"
m = f(i)

print(m)

#4
import re

def f(s):
    p = r'[A-Z][a-z]+'
    m = re.findall(p, s)
    return m

i = "example"
m = f(i)

print(m)

#5
import re

def m(s):
    p = '^a.*b$'
    return bool(re.search(p, s))

t = "a anything b"
m(t)

#6
import re

def r(s):
    return re.sub('[ ,.]', ':', s)

t = "Hello, World."
r(t)

#7
def s2c(s):
    return ''.join(w.capitalize() or '_' for w in s.split('_'))

t = "this_sdgg_dh."
s2c(t)

#8
import re

def sp_upper(s):
    return re.findall('[A-Z][^A-Z]*', s)

t = "SampleText"
sp_upper(t)

#9
def insert_spaces(s):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)

t = "HelloWorld"
insert_spaces(t)

#10
def c2s(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

t = "CamelCase"
c2s(t)






