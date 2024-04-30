import itertools
import time
from multiprocessing import Process, synchronize, Event


def slow() -> int:
    time.sleep(3)
    return 42


def spin1(msg: str, done: synchronize.Event) -> None:
    status = None
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end=' ', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}', end=' ')


def supervisor1() -> int:
    done = Event()
    spinner = Process(target=spin1, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    res = slow()
    done.set()
    spinner.join()
    return res


if __name__ == '__main__':
    result = supervisor1()
    print(f'\rAnswer:{result}', flush=True)
