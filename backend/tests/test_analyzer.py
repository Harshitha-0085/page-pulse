import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analyzer import analyze_url

def test_invalid_url():
    result = analyze_url("google.com")

    assert "error" in result


def test_valid_url():
    result = analyze_url("https://example.com")

    assert result["http_status"] == 200
    assert result["page_title"] == "Example Domain"
    assert result["h1_count"] == 1
def test_connection_error():
    result = analyze_url("https://this-domain-does-not-exist-123456789.com")

    assert "error" in result