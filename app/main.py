import logging.config

from app.logging_setup import logging_setup

logger = logging.getLogger(__name__)


def main() -> None:
    logging_setup()


if __name__ == "__main__":
    main()
