import requests
from openai import OpenAI
import os
import logging


class GetVisualization:
    def __init__(self):
        openai_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=openai_key)
        self.logger = logging.getLogger(__name__)

    def send_text_get_image(self, text):
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=text,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url
            self.logger.info(
                f"Image generated successfully text={text}, image_url={image_url}"
            )
            return image_url
        except requests.RequestException as e:
            self.logger.error(f"Error communicating with server: {e}")
            return None
