import httpx
import json

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

def parser_exploreUrl(explore_url):
    results = []
    if not explore_url or explore_url.startswith('@js:'):
        return results

    if '::' in explore_url:
        lines = explore_url.strip().split('\n')
        for line in lines:
            if '::' in line:
                name, url = line.split('::', 1)
                results.append({'name': name.strip(), 'url': url.strip()})

    elif '{' in explore_url and '}' in explore_url:
        try:
            explore_list = json.loads(explore_url)
            for item in explore_list:
                name = item.get('title')
                url = item.get('url')
                if name and url:
                    results.append({'name': name, 'url': url})
        except json.JSONDecodeError:
            pass
    return results

async def fetch_explore_url_async(explore_url, page=1):
    result = []
    if '{{page}}' in explore_url:
        explore_url = explore_url.replace('{{page}}', str(page))
    data = await fetch_json_async(explore_url)
    return data