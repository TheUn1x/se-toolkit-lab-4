"""End-to-end tests for the GET /interactions endpoint."""

import httpx


def test_get_interactions_returns_200(api_base_url: str, api_token: str) -> None:
    """GET /interactions/ returns HTTP status code 200."""
    with httpx.Client() as client:
        response = client.get(
            f"{api_base_url}/interactions/",
            headers={"Authorization": f"Bearer {api_token}"}
        )
        assert response.status_code == 200


def test_get_interactions_response_is_a_list(api_base_url: str, api_token: str) -> None:
    """GET /interactions/ response body is a JSON array."""
    with httpx.Client() as client:
        response = client.get(
            f"{api_base_url}/interactions/",
            headers={"Authorization": f"Bearer {api_token}"}
        )
        assert isinstance(response.json(), list)
