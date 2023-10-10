# pylint: skip-file

import pytest

from countries import fetch_data, APIError


class TestFetchData:
    """Contains tests of the fetch_data function."""

    def test_calls_requests_get_method(self, requests_mock):
        """Tests that fetch_data makes exactly one GET request."""
        requests_mock.get("https://restcountries.com/v3.1/name/test", status_code=200, json={})
        fetch_data("test")

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    def test_returns_a_valid_dict(self, requests_mock):
        """Checks that fetch_data returns a valid dict with relevant keys."""
        requests_mock.get("https://restcountries.com/v3.1/name/test", status_code=200, json={
            "name": {
                "official": "Testopia"
            },
            "flag": "test",
            "languages": {
              "test": "Testian"
            },
        })
        res = fetch_data("test")

        assert isinstance(res, dict)
        assert "name" in res and isinstance(res["name"], dict)
        assert "flag" in res
        assert "languages" in res and isinstance(res["languages"], dict)

    def test_raises_404_error(self, requests_mock):
        """Checks that fetch_data raises the correct error upon a 404 response."""
        requests_mock.get("https://restcountries.com/v3.1/name/test", status_code=404)
        with pytest.raises(APIError) as exception:
            fetch_data("test")
        
        assert exception.value.message == "Unable to locate matching country."
        assert exception.value.code == 404

    def test_raises_500_error(self, requests_mock):
        """Checks that fetch_data raises the correct error upon a 500 response."""
        requests_mock.get("https://restcountries.com/v3.1/name/test", status_code=500)
        with pytest.raises(APIError) as exception:
            fetch_data("test")

        assert exception.value.message == "Unable to connect to server."
        assert exception.value.code == 500
