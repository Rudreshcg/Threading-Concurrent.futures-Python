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


#MUlti-threading
import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'{threading.current_thread().name} Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done Sleeping...{seconds} second(s)...')


threads = []
for _ in range(1, 6):
    t = threading.Thread(target=do_something, args=[_])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

#OUTPUT:-
# Thread-1 (do_something) Sleeping 1 second(s)...
# Thread-2 (do_something) Sleeping 2 second(s)...
# Thread-3 (do_something) Sleeping 3 second(s)...
# Thread-4 (do_something) Sleeping 4 second(s)...
# Thread-5 (do_something) Sleeping 5 second(s)...
# Done Sleeping...1 second(s)...
# Done Sleeping...2 second(s)...
# Done Sleeping...3 second(s)...
# Done Sleeping...4 second(s)...
# Done Sleeping...5 second(s)...
# Finished in 5.01 second(s)
