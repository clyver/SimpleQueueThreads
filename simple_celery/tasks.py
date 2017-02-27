from celery_app import app


@app.task
def iterative_fib(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a
