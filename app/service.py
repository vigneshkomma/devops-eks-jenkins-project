import time
import httpx
from app.schemas import URLCreate

monitored_urls = []
next_id = 1


def add_url(data: URLCreate):
    global next_id

    new_url = {
        "id":next_id,
        "name": data.name,
        "url": str(data.url)
    }

    monitored_urls.append(new_url)
    next_id +=1

    return new_url

def get_urls():
    return monitored_urls

def get_url(url_id: int):
    for item in monitored_urls:
        if item["id"] == url_id:
            return item
    
    return None

def delete_url(url_id: int):
    item = get_url(url_id)

    if item is None:
        return None
    
    monitored_urls.remove(item)
    return item

def check_url(item):
    
    start_time = time.perf_counter()

    try:
        response = httpx.get(item["url"],timeout=5)
        response_time = round((time.perf_counter()-start_time) * 1000, 2)

        return {
            "id": item["id"],
            "name": item["name"],
            "url": item["url"],
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "is_healthy": 200 <= response.status_code < 400,
            "error": None
        }
    except Exception as error:

        response_time = round((time.perf_counter() - start_time) * 1000, 2)

        return {
            "id": item["id"],
            "name": item["name"],
            "url": item["url"],
            "status_code": None,
            "response_time_ms": response_time,
            "is_healthy": False,
            "error": str(error)
        }

def run_all_checks():
    return [check_url(item) for item in monitored_urls]     