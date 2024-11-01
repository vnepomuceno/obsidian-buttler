import logging

import coloredlogs


def get_logger(name: str) -> logging.Logger:
    coloredlogs.install()
    custom_logger = logging.getLogger(name)
    logging.SUCCESS = 25  # between WARNING and INFO
    logging.addLevelName(logging.SUCCESS, "SUCCESS")
    setattr(
        custom_logger,
        "success",
        lambda message, *args: custom_logger._log(logging.SUCCESS, message, args),
    )
    coloredlogs.install(
        level="INFO",
        logger=custom_logger,
        fmt="%(asctime)s [%(name)s] <%(levelname)s> %(message)s",
    )

    return custom_logger


logger = get_logger(__name__)