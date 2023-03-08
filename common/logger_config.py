import logging


class Logger(logging.Logger):
    __INSTANCE = None

    def __init__(self):
        super().__init__(name="")

        self.setLevel(logging.INFO)

        formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s: %(message)s')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

    def __new__(cls):
        """ 싱글톤 패턴 처리
        """
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(logging.Logger, cls).__new__(cls)
        return cls.__INSTANCE