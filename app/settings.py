import base64
import os
import logging
import uuid

from pydantic_settings import BaseSettings


DEBUG = True

APP_DIR = os.path.dirname(__file__)


class Settings(BaseSettings):
    """Settings for the app."""
    server_host: str = os.environ.get("LESTA_API_ADDRESS", "localhost")
    server_port: int = int(os.environ.get("LESTA_API_PORT", 8080))
    application_id: str = os.environ.get("LESTA_API_APP_ID", "")
    log_directory: str = os.environ.get("LESTA_API_LOG_DIR", 'logs')  # recommended /var/log/lesta-api/
    log_name: str = os.environ.get("LESTA_API_LOG_NAME", "default.log")
    debug: bool = os.environ.get("LESTA_API_DEBUG", True if 1 else False)

    # def post_init(self):
    #     """Method called after initialization."""
    #     self.setup_logging()

    # def setup_logging(self):
    #     """Set up logging configuration."""
    #     os.makedirs(self.log_directory, exist_ok=True)
    #     level = logging.DEBUG if self.debug else logging.INFO
    #     logging.basicConfig(
    #         level=level,
    #         filename=os.path.join(self.log_directory, self.log_name),
    #         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #         datefmt='%d.%m.%Y %H:%M:%S'
    #     )
    #     context_id = str(uuid.uuid4())[:8]
    #     return logging.getLogger('[lesta-api] [{}]'.format(context_id))


# Initialize settings
settings = Settings()
