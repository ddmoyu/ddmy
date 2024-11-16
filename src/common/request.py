import httpx

async def fetch_json_async(url):
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(10.0), follow_redirects=True) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except (httpx.HTTPStatusError, httpx.ReadTimeout) as exc:
        print(f"An error occurred while fetching the URL: {exc}")
    except httpx.RequestError as exc:
        print(f"An error occurred while making the request: {exc}")
    return None

async def fetch_text_async(url):
    try:
        cookies = {
            'PHPSESSID': 'g22ilus0s52inphq272ggvq3na'
        }
        headers = {
            'authority': 'www.zhongyi6.com',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.zhongyi6.com/chapter/read/1734/36969',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        async with httpx.AsyncClient(timeout=httpx.Timeout(10.0), follow_redirects=True, cookies=cookies, headers=headers) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
    except (httpx.HTTPStatusError, httpx.ReadTimeout) as exc:
        print(f"An error occurred while fetching the URL: {exc}")
    except httpx.RequestError as exc:
        print(f"An error occurred while making the request: {exc}")
    return None
