import urllib.request

def gather_input_data(url, sessionId, transform=lambda x: str(x, "utf-8").strip('\n')):
    request = urllib.request.Request(url)
    request.add_header("cookie", "session={}".format(sessionId)) # Source the data directly from AoC

    values = []
    with urllib.request.urlopen(request) as data:
        for line in data:
            values.append(transform(line))

    return values