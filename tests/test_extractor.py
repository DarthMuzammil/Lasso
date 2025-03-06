import pytest
from src.extractor import LLMCodeExtractor
from src.exceptions import LLMOutputException
import re

extractor = LLMCodeExtractor()

def test_extract_valid_code():
    match = re.match(r"```(\w+)\s+//([\w\d_-]+\.\w+)\s+(.*?)```", "```python //example.py print('Hello')```", re.DOTALL)
    print("match", match)
    code_block = extractor.extract(match)
    assert code_block.filename == "example.py"
    assert code_block.extension == "python"
    assert code_block.code == "print('Hello')"

def test_filename_extension_mismatch():
    match = re.match(r"```(\w+)\s+//([\w\d_-]+\.\w+)\s+(.*?)```", "```python //example.js print('Hello')```", re.DOTALL)
    with pytest.raises(LLMOutputException):
        extractor.extract(match)
