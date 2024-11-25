import logging
import logging.config
from src.ports.logger.logger_port import LoggerPort
from src.infrastructure.utils.context import get_trace_id
logging.config.fileConfig("src/log.conf")
class LoggerAdapter(LoggerPort):
    def __init__(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)

    def _format_message(self, message: str) -> str:
        trace_id = get_trace_id()
        return f"[TraceID: {trace_id}] {message}"

    def info(self, message: str):
        self.logger.info(self._format_message(message))

    def error(self, message: str):
        self.logger.error(self._format_message(message))

    def debug(self, message: str):
        self.logger.debug(self._format_message(message))
    
    def warning(self, message: str):
        self.logger.warning(self._format_message(message))
    
    def critical(self, message: str):
        self.logger.critical(self._format_message(message))
        
    def exception(self, message: str):
        self.logger.exception(self._format_message(message))

# Singleton logger instance
_logger_instance = LoggerAdapter("")

def get_logger() -> LoggerPort:
    """Provide a global logger instance."""
    return _logger_instance