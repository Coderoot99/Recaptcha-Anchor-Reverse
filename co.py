import base64

def co(site):
    site = f"https://{site}:443"
    co = base64.b64encode(site.encode()).decode()
    return co
