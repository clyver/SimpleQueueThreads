from threading import Thread
import timeit

from labor import recursive_fib as slow_task, recursive_fib_cached as fast_task


def do_work(task, weight, thread_name):

    print "{} beginning work...\n".format(thread_name)
    start_time = timeit.default_timer()
    task(weight)
    end_time = timeit.default_timer()
    print "{} completed work in {} seconds\n".format(thread_name, end_time-start_time)


fast_thread = Thread(target=do_work, args=(fast_task, 30, "FastThread"))
slow_thread = Thread(target=do_work, args=(slow_task, 30, "SlowThread"))

# Fast thread will finish before the slow thread, even if got a late start.
slow_thread.start()
fast_thread.start()
