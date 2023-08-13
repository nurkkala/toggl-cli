import os

import httpx

print(os.getenv("TOGGL_API_TOKEN"))


def who_am_i():
    result = httpx.get(
        "https://api.track.toggl.com/api/v9/me",
        auth=(os.getenv("TOGGL_API_TOKEN"), "api_token"),
    )
    return result.json()


def time_entries():
    result = httpx.get(
        "https://api.track.toggl.com/api/v9/me/time_entries",
        auth=(os.getenv("TOGGL_API_TOKEN"), "api_token"),
        params={"start_date": "2023-08-08", "end_date": "2023-08-11"},
    )
    return result.json()


def list_projects():
    result = httpx.get(
        "https://api.track.toggl.com/api/v9/me/projects",
        auth=(os.getenv("TOGGL_API_TOKEN"), "api_token"),
    )
    return result.json()


def list_clients():
    result = httpx.get(
        "https://api.track.toggl.com/api/v9/me/clients",
        auth=(os.getenv("TOGGL_API_TOKEN"), "api_token"),
    )
    return result.json()
