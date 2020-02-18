import threading

# global variable x
x = 0


def increment():
    """function to increment global variable x by 1"""
    global x
    x += 1


def thread_task():
    """task for thread calls increment function 1000000 times"""
    for _ in range(1000000):
        increment()


def main_task():
    """Two threads t1 and t2 are created in main_task function and global variable x is set to 0.
Each thread has a target function thread_task in which increment function is called 100000 times.
increment function will increment the global variable x by 1 in each call."""
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)
    global x
    # setting global variable x as 0
    x = 0

    # start the threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0} : x = {1}".format(i, x))
