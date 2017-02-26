import timeit


def recursive_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


def memoize(f):
    cache = {}

    def decorated_function(arg):
        if arg in cache:
            return cache[arg]
        else:
            cache[arg] = f(arg)
            return cache[arg]
    return decorated_function


@memoize
def recursive_fib_cached(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive_fib_cached(n-1) + recursive_fib_cached(n-2)


def iterative_fib(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a


def demonstrate_load():
    print "* Running 3 variants of fibonacci, set to calculate the 37th fibonacci number..."
    test_scenarios = [
        ('naive recursive implementation', recursive_fib),
        ('recursive implementation with a cache', recursive_fib_cached),
        ('iterative implementation', iterative_fib)
    ]

    for test_description, fib_test in test_scenarios:
        print "#" * 20
        print "Running {} ...".format(test_description)
        start_time = timeit.default_timer()
        fib_test(37)
        end_time = timeit.default_timer()
        print "{} took {} seconds to complete".format(test_description, end_time-start_time)

# demonstrate_load()
