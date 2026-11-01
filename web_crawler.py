
from urllib.request import Request, urlopen
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href" and value:
                    self.links.append(value)

def run(target):
    base = f"https://{target}/"
    visited = set()
    queue = [base]

    while queue and len(visited) < 20:
        url = queue.pop(0)
        if url in visited:
            continue

        if urlparse(url).hostname != target:
            continue

        visited.add(url)

        try:
            request = Request(
                url, headers={"User-Agent": "WebReconX-Lab/1.0"}
            )
            with urlopen(request, timeout=5) as response:
                content_type = response.headers.get("Content-Type", "")
                if "text/html" not in content_type:
                    continue
                html = response.read(500_000).decode("utf-8", errors="replace")

            parser = LinkParser()
            parser.feed(html)

            for link in parser.links:
                absolute = urljoin(url, link)
                parsed = urlparse(absolute)

                if (parsed.scheme == "https"
                        and parsed.hostname == target
                        and absolute not in visited
                        and absolute not in queue):
                    queue.append(absolute)

            print("Visited:", url)

        except Exception as error:
            print(f"Could not crawl {url}: {error}")

    result = sorted(visited)
    print(f"Pages visited: {len(result)}")
    return result
