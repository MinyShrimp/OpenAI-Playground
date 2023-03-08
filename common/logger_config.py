import logging

'''
Since: 2023-03-09
Author: 김회민 ksk7584@gmail.com
'''


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;5;244m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Logger(logging.Logger):
    __INSTANCE = None

    def __init__(self):
        super().__init__(name="")

        self.setLevel(logging.DEBUG)
        formatter = CustomFormatter('[%(asctime)s] %(levelname)7s: %(filename)20s - %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

    def __new__(cls):
        """ 싱글톤 패턴 처리
        """
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(logging.Logger, cls).__new__(cls)
        return cls.__INSTANCE


log = Logger()
