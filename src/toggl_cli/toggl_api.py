import os
from functools import cache
from typing import Any, Optional

import httpx
import pendulum
from pendulum import DateTime


@cache
def http_client():
    toggl_api_token = os.getenv("TOGGL_API_TOKEN")
    assert toggl_api_token is not None

    return httpx.Client(
        base_url="https://api.track.toggl.com/api/v9",
        auth=(toggl_api_token, "api_token"),
    )


def who_am_i() -> Any:
    return http_client().get("/me").json()


def time_entries(
    start_date: Optional[DateTime] = None, end_date: Optional[DateTime] = None
) -> Any:
    if start_date is None:
        start_date = pendulum.today().subtract(days=3)
    if end_date is None:
        end_date = pendulum.today()

    return (
        http_client()
        .get(
            "/me/time_entries",
            params={
                "start_date": start_date.to_date_string(),
                "end_date": end_date.to_date_string(),
            },
        )
        .json()
    )


def list_projects() -> Any:
    return http_client().get("/me/projects").json()


def list_clients() -> Any:
    return http_client().get("/me/clients").json()
