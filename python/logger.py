import logging
import os
import threading
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from typing import Optional


class AsyncLogHandler(logging.Handler):
    def __init__(self, log_dir: str = 'logs', max_size_mb: int = 10):
        super().__init__()
        self.log_dir = log_dir
        self.max_size = max_size_mb * 1024 * 1024
        os.makedirs(log_dir, exist_ok=True)
        self._lock = threading.Lock()
        self._setup_handler()

    def _setup_handler(self):
        filename = os.path.join(self.log_dir, f'{datetime.now().strftime("%Y%m%d")}.log')
        self.handler = TimedRotatingFileHandler(
            filename=filename,
            when='midnight',
            interval=1,
            backupCount=7,
            encoding='utf-8'
        )
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    def emit(self, record):
        with self._lock:
            try:
                if os.path.getsize(self.handler.baseFilename) > self.max_size:
                    self.handler.doRollover()
                self.handler.emit(record)
            except Exception as e:
                print(f"日志写入失败: {str(e)}")


class RouterLogger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.logger = logging.getLogger('RouterLogger')
                cls._instance.logger.setLevel(logging.INFO)
                cls._instance.logger.addHandler(AsyncLogHandler())
            return cls._instance

    @classmethod
    def log_operation(cls, operation_type: str, details: str, success: bool = True):
        logger = cls().logger
        status = "SUCCESS" if success else "FAILED"
        log_msg = f"{operation_type} - {status} - {details}"
        logger.info(log_msg)

    @classmethod
    def log_error(cls, error_msg: str, exception: Optional[Exception] = None):
        logger = cls().logger
        error_details = f"{error_msg}"
        if exception:
            error_details += f" | Exception: {str(exception)}"
        logger.error(error_details)
