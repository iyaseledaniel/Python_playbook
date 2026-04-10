# program that uses async and await keywords for concurrency

import asyncio
async def main():
    print('Hello, welcome to learning python in 12 weeks')
    await asyncio.sleep(1)
    print('From zero to Mastery')
    await asyncio.sleep(3)
    print('This is a starting phase')

asyncio.run(main())
help("fractions")