import logging
from abc import ABC, abstractmethod
from .exceptions import LLMOutputException
from collections import namedtuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CodeBlock = namedtuple("CodeBlock", ["filename", "extension", "code"])

class CodeExtractor(ABC):
    """Abstract base class for extracting details from LLM output."""
    
    @abstractmethod
    def extract(self, match) -> CodeBlock:
        pass

class LLMCodeExtractor(CodeExtractor):
    """Extracts filename, extension, and code content."""

    def extract(self, match) -> CodeBlock:
        extension, filename, code_content = match.groups()

        if not filename.endswith(f".{extension}"):
            logger.error(f"Filename '{filename}' and extension '{extension}' do not match.")
            raise LLMOutputException("Filename and extension mismatch.")

        return CodeBlock(filename=filename, extension=extension, code=code_content.strip())
