from typing import Dict, Any
import json
import requests
from config import BASE_URL, TOKEN


def get_hero_by_id(hero_id: str) -> Dict[str, Any]:
    """
    Retrieve hero information by ID from the specified API.

    Parameters:
        hero_id (str): The ID of the hero to retrieve.

    Returns:
        Dict[str, Any]: A dictionary containing hero information.

    Raises:
        requests.exceptions.HTTPError: If the API response indicates an error.
    """
    request_url = f'{BASE_URL}{TOKEN}/{hero_id}'
    response = requests.get(request_url)
    response.raise_for_status()
    response_content = json.loads(response.content)
    if response_content['response'] == 'error':
        raise requests.exceptions.HTTPError(f"API Error: {response_content['error']}")
    return response_content
