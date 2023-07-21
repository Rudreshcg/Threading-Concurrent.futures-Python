#Single threading
import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'{threading.current_thread().name} Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds} second(s)...'


print(do_something(5))
print(do_something(4))
print(do_something(3))
print(do_something(2))
print(do_something(1))

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')


#OUTPUT:-
# MainThread Sleeping 5 second(s)...
# Done Sleeping...5 second(s)...
# MainThread Sleeping 4 second(s)...
# Done Sleeping...4 second(s)...
# MainThread Sleeping 3 second(s)...
# Done Sleeping...3 second(s)...
# MainThread Sleeping 2 second(s)...
# Done Sleeping...2 second(s)...
# MainThread Sleeping 1 second(s)...
# Done Sleeping...1 second(s)...
# Finished in 15.02 second(s)
