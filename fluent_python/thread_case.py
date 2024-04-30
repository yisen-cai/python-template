import itertools
import time
from threading import Event, Thread


def spin(msg: str, done: Event) -> None:
    status = None
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end=' ', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}', end=' ')


def slow() -> int:
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    # Create a thread.
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    res = slow()
    # Terminate the thread.
    done.set()
    # Wait until spinner thread finishes.
    spinner.join()
    return res


if __name__ == '__main__':
    result = supervisor()
    print(f'\rAnswer:{result}', flush=True)
