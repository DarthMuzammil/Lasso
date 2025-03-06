from .validator import LLMOutputValidator
from .extractor import LLMCodeExtractor
from .exceptions import LLMOutputException
from collections import namedtuple
CodeBlock = namedtuple("CodeBlock", ["filename", "extension", "code"])
class LLMOutputProcessor:
    """Processor for validating and extracting LLM-generated code output."""

    def __init__(self, validator: LLMOutputValidator, extractor: LLMCodeExtractor):
        self.validator = validator
        self.extractor = extractor

    def process(self, text: str):
        """Validates and extracts LLM output."""
        match = self.validator.validate(text)
        return self.extractor.extract(match)

# Instantiate components
validator = LLMOutputValidator()
extractor = LLMCodeExtractor()
processor = LLMOutputProcessor(validator, extractor)
