# My Demo Agent

## Purpose

`my-demo-agent` is a lightweight demonstration agent that showcases how to interact with a repository using AI-driven tools. It provides simple examples of reading files, searching code, and performing basic operations, making it a useful reference for developers building similar automation agents.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/my-demo-agent.git
   cd my-demo-agent
   ```
2. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *If a `requirements.txt` file does not exist, install the required packages manually (e.g., `openai`, `requests`).*

## Usage

The agent interacts with the repository through a set of predefined functions. The main entry point for demonstration purposes is `demo.py`.

```bash
python demo.py
```

Running the script will showcase examples such as:
- Listing files in the repository
- Reading file contents
- Searching for code snippets
- Creating and updating files

## Examples

Below are a few typical usage scenarios you might find in `demo.py`:

```python
# List all files in the main branch
files = get_main_branch_files_overview()
print(files)

# Read a specific file
content = read_file({"formatted_filepath": "demo.py"})
print(content)

# Search for a function definition
results = search_code({"search_query": "def my_function"})
print(results)
```

Feel free to extend `demo.py` or create your own scripts that leverage the provided functions.

## Contributing

Contributions are welcome! To contribute:
1. **Fork the repository**
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and ensure they follow the existing coding style.
4. **Write or update documentation** (including this README) as needed.
5. **Commit your changes** with clear messages:
   ```bash
   git commit -m "Add feature X" 
   ```
6. **Push to your fork** and open a Pull Request.

Please make sure that any new code is accompanied by appropriate tests and that all existing tests pass.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.