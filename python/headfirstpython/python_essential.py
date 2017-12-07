"""
lambda
"""

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4,0,1,5,6]
print(apply_to_list(ints, lambda x:x*2))


strings = ['foo', 'card', 'bar', 'aaa', 'abab']
print(len(set(strings)))
strings.sort(key=lambda x:len(set(list(x))))
print(strings)


"""
closure
"""

def make_closure(a):
    def closure():
        print('I know the secrte: %d' %a)
    return closure

closure = make_closure(4)
print(closure())


def make_watcher():
    have_seen = {}

    def has_been_seen(x):
        if x in have_seen:
            return True
        else:
            have_seen[x] = True
            return False

    return has_been_seen

watcher = make_watcher()
vales = [5,6,1,5,1,6,3,5]

print([watcher(val) for val in vales])


def format_and_pad(template, space):
    def formatter(x):
        return (template % x).rjust(space)

    return formatter


def say_hello_then_call_f(f, *args, **kwargs):
    print('args is',args)
    print('kwargs is',kwargs)
    print("Hello! Now I'm going to call %s" % f)
    return f(*args, **kwargs)

def g(x,y,z=1):
    return (x+y) / z

"""
currying
"""




