# Lasso

[![PyPI](https://img.shields.io/pypi/v/lasso.svg)](https://pypi.org/project/lasso/)
[![License](https://img.shields.io/github/license/DarthMuzammil/Lasso)](LICENSE)

Lasso is a Python package designed to extract code snippets from plain text using Large Language Models (LLMs).

## Installation

Install via pip:

```sh
pip install lasso
```

## Usage
### python
```py
from lasso import extractor

text = "Here's some Python code: print('Hello World')"
code_snippet = extractor.extract_code(text)
print(code_snippet)
```

## Features
- Extracts code snippets from plain text.
- Supports multiple programming languages.
- Easily integrates into other LLM-based projects.

## Contributing
- Fork the repository.
- Clone it: git clone https://github.com/DarthMuzammil/Lasso.git
- Install dependencies: pip install -r requirements.txt
- Submit a pull request!

## License
This project is licensed under the MIT License.

## Next Steps
1. Make sure `src/lasso/__init__.py` exists.
2. Create `pyproject.toml` (or use `setup.py` if preferred).
3. Build and upload to PyPI using `twine`.

Let me know if you need help with any step! 🚀
