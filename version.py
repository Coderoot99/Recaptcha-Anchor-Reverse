import requests

def version():
    r = requests.get("https://www.google.com/recaptcha/api.js")
    version = re.search(
        r"https://www\.gstatic\.com/recaptcha/releases/([a-zA-Z0-9_-]+)/", r.text
    ).group(1)
    return version
