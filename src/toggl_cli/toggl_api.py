import os

import httpx

print(os.getenv("TOGGL_API_TOKEN"))


def who_am_i():
    result = httpx.get(
        "https://api.track.toggl.com/api/v9/me",
        auth=(os.getenv("TOGGL_API_TOKEN"), "api_token"),
    )
    return result.json()
