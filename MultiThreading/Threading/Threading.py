# import threading
# import time
#
# start = time.perf_counter()
#
#
# def do_something(seconds):
#     print(f'sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     print('done sleeping...')
#
#
# threads = []
# for _ in range(10):
#     thread = threading.Thread(target=do_something, args=[1.5])
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# finish = time.perf_counter()
#
# print(f'Finished in {round(finish - start, 2)} second(s)')


import concurrent.futures
import threading
import time

start = time.perf_counter()


def do_something(second):
    print(f'sleeping {second} second(s)...')
    time.sleep(second)
    return f'done sleeping...{second}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, second) for second in seconds]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executor.map(do_something, seconds)

    # for result in results:
    #     print(result)

# threads = []
# for _ in range(10):
#     thread = threading.Thread(target=do_something, args=[1.5])
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
