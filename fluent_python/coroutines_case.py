import asyncio
import itertools


async def spin(msg: str):
    status = None
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end=' ')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end=' ')


async def slow() -> int:
    await asyncio.sleep(3)
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking'))
    print(f'spinner object: {spinner}')
    res = await slow()
    spinner.cancel()
    return res


if __name__ == '__main__':
    result = asyncio.run(supervisor())
    print(f'\rAnswer: {result}')
