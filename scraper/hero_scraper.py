from typing import Dict, Any
from utils import download_hero_img


def process_hero_response(response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process the hero response by removing unnecessary fields and downloading the hero image.

    Parameters:
        response (Dict[str, Any]): The hero response data.

    Returns:
        Dict[str, Any]: The processed hero response with the image URL updated.
    """
    response.pop('response')
    response.pop('id')
    image_url = download_hero_img(response['name'], response['image']['url'])
    response['image']['url'] = image_url
    return response
