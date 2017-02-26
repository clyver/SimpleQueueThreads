from collections import defaultdict
from Queue import Queue
from random import randint
from threading import Thread
from timeit import default_timer

from labor import recursive_fib_cached as fast_task

q = Queue()
num_tasks = 500000
num_workers = 5
task_counts = defaultdict(int)


def worker(name):
    while not q.empty():
        task, weight = q.get()
        task(weight)
        q.task_done()
        task_counts[name] += 1

print "* Loading the queue with tasks..."
for _ in xrange(num_tasks):
    # Assign a random weight to each task
    q.put((fast_task, randint(0, 500)))
print "* Queue loaded with {} tasks...".format(num_tasks)

print "* Establishing workers..."
workers = []
for i in xrange(num_workers):
    worker_name = "Worker {}".format(i)
    t = Thread(target=worker, args=[worker_name])
    t.daemon = True
    workers.append(t)
start_time = default_timer()
[worker.start() for worker in workers]
print "* {} workers established to tackle queue...".format(num_workers)

q.join()

print "* Work complete!"
end_time = default_timer()
t_delta = end_time - start_time
print "*" * 80
print "Summary: {} workers completed {} tasks in {} seconds".format(num_workers, num_tasks, t_delta)
for worker, num_tasks_accomplished in sorted(task_counts.items(), key=lambda x: x[1], reverse=True):
    print "{} accomplished {} tasks".format(worker, num_tasks_accomplished)
