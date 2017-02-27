from timeit import default_timer

from tasks import iterative_fib


def demonstrate_task(val):
    check_ins = 0
    start_time = default_timer()
    result = iterative_fib.delay(val)
    while not result.ready():
        check_ins += 1
    t_delta = default_timer() - start_time

    print "Celery worker calculated {}th fib number in {} " \
          "seconds after {} check-ins".format(val, t_delta, check_ins)

demonstrate_task(10000)
