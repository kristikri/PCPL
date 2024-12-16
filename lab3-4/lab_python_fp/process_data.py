import json
import sys
import time
from contextlib import contextmanager

path = "C:/Users/ann18/OneDrive/Desktop/bmstu/3sem/PCPL/lab3-4/lab_python_fp/data_light.json"

with open(path, encoding="utf8") as f:
    data = json.load(f)

@contextmanager
def cm_timer_1():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"time: {elapsed_time}")

def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@print_result
def f1(arg):
    return sorted(list(set([job['job-name'].lower() for job in arg])))

@print_result
def f2(arg):
    return list(filter(lambda job: job.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda job: job + ', с опытом Python', arg))

@print_result
def f4(arg):
    salary = [str(i) for i in range(100000, 200001)]
    return list(zip(arg, salary))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))