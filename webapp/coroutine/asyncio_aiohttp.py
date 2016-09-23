import asyncio
import aiohttp
import bs4
import tqdm
"""
async ==> @asyncio.coroutine
await ==> yield from
"""


async def get(url):
    response = await aiohttp.request('GET', url)
    body = await response.read_and_close(decode=True)
    print(body)

async def wait_with_progress(coros):
    for f in tqdm.tqdm(asyncio.as_completed(coros), total=len(coros)):
        await f


def first_magnet(page):
    soup = bs4.BeautifulSoup(page)
    a = soup.find('a', title='Download this torrent using magnet')
    return a['href']

async def print_magnet(query):
    url = 'http://thepiratebay.se/search/{}/0/7/0'.format(query)
    with (await sem):
        page = await get(url)
    magnet = first_magnet(page)
    print('{}: {}'.format(query, magnet))


distros = ['archlinux', 'ubuntu', 'debian']
sem = asyncio.Semaphore(5)
loop = asyncio.get_event_loop()
f = asyncio.wait([print_magnet(d) for d in distros])
loop.run_until_complete(f)
