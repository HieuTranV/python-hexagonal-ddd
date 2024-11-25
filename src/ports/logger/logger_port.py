from abc import ABC, abstractmethod

class LoggerPort(ABC):
    @abstractmethod
    def info(self, message: str):
        """Log an informational message."""
        pass

    @abstractmethod
    def error(self, message: str):
        """Log an error message."""
        pass

    @abstractmethod
    def debug(self, message: str):
        """Log a debug message."""
        pass
    
    @abstractmethod
    def warning(self, message: str):
        """Log a warning message."""
        pass
    
    @abstractmethod
    def critical(self, message: str):
        """Log a critical message."""
        pass

    @abstractmethod
    def exception(self, message: str):
        """Log an exception message."""
        pass