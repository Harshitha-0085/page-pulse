import time
import requests
from bs4 import BeautifulSoup
REQUEST_TIMEOUT = 10

def analyze_url(url):
    try:
        start_time = time.time()

        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        if response.status_code >= 400:
            return {
                "error": f"Website returned HTTP {response.status_code}"
         }

        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        if "text/html" not in response.headers.get("Content-Type", ""):
            return {
                "error": "URL did not return an HTML page."
            }

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No title"

        meta = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta.get("content").strip()
            if meta and meta.get("content")
            else "No meta description"
        )

        h1_count = len(soup.find_all("h1"))

        images = soup.find_all("img")
        missing_alt = sum(
            1
            for img in images
            if not img.get("alt") or img.get("alt").strip() == ""
        )

        words = soup.get_text(separator=" ", strip=True).split()

        return {
            "url": url,
            "http_status": response.status_code,
            "response_time_ms": response_time,
            "page_title": title,
            "meta_description": meta_description,
            "h1_count": h1_count,
            "images_missing_alt": missing_alt,
            "word_count": len(words),
        }

    except requests.exceptions.MissingSchema:
        return {"error": "Please include http:// or https:// in the URL."}

    except requests.exceptions.ConnectionError:
        return {"error": "Unable to connect to the website."}

    except requests.exceptions.Timeout:
        return {"error": "The request timed out."}

    except Exception as e:
        return {"error": str(e)}