
# Wealth App API Testing

Welcome to the **Wealth App API Testing** repository. This project contains automated tests for validating the API endpoints of the Wealth App's Master Data module. The tests are written using `pytest` with `pytest-bdd` for Behavior-Driven Development (BDD) style testing. This README provides instructions on how to set up, run, and customize the test executions.

## Table of Contents

- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Running Tests](#running-tests)
  - [Basic Test Execution](#basic-test-execution)
  - [Running Specific Tests with `-m`](#running-specific-tests-with--m)
  - [Enhanced Reporting](#enhanced-reporting)
- [Key Pytest Options](#key-pytest-options)
- [Writing Tests](#writing-tests)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the testing environment, follow these steps:

1. **Clone the Repository:**

   \`\`\`bash
   git clone https://github.com/yourusername/wealth-app-api-testing.git
   cd wealth-app-api-testing
   \`\`\`

2. **Create a Virtual Environment:**

   \`\`\`bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scriptsctivate`
   \`\`\`

3. **Install Dependencies:**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Directory Structure

The project is organized as follows:

\`\`\`
Wealth_App/
  ├── tests/
  │   ├── AddressTypeTests/
  │   │   └── test_GET_fetchAddressTypes.py
  │   ├── features/
  │   │   └── fetch_address_types.feature
  ├── configs/
  │   └── apis_endpoint.py
  └── README.md
\`\`\`

- **\`tests/\`**: Contains the Python test scripts.
- **\`features/\`**: Contains the Gherkin feature files.
- **\`configs/\`**: Configuration files, including API endpoints.
- **\`README.md\`**: This README file.

## Running Tests

### Basic Test Execution

To run all tests, simply use:

\`\`\`bash
pytest
\`\`\`

This command will discover and run all the tests in the \`tests/\` directory.

### Running Specific Tests with \`-m\`

You can run specific tests based on the markers (tags) applied to them. For example, to run only the tests marked as \`regression\`:

\`\`\`bash
pytest -m regression
\`\`\`

This command filters and executes only those tests that have been marked with \`@pytest.mark.regression\`.

### Enhanced Reporting

For more detailed and readable output, you can use the \`--gherkin-terminal-reporter\` option, which provides a Gherkin-style report in the terminal:

\`\`\`bash
pytest --gherkin-terminal-reporter
\`\`\`

To generate a JSON report in the Cucumber format:

\`\`\`bash
pytest --cucumberjson=cucumber.json
\`\`\`

This generates a \`cucumber.json\` report file that can be used for integration with other tools or dashboards.

## Key Pytest Options

### \`-m <marker>\`

- **Usage**: Filters tests based on the specified marker.
- **Example**: \`pytest -m regression\`
- **Explanation**: Runs only the tests that are tagged with the \`regression\` marker.

### \`--gherkin-terminal-reporter\`

- **Usage**: Provides a Gherkin-style output in the terminal.
- **Example**: \`pytest --gherkin-terminal-reporter\`
- **Explanation**: Useful for viewing the test scenarios in a more human-readable format, similar to the Gherkin syntax.

### \`--cucumberjson=<file>\`

- **Usage**: Generates a Cucumber JSON report.
- **Example**: \`pytest --cucumberjson=cucumber.json\`
- **Explanation**: Produces a JSON report that is compatible with Cucumber, useful for integration with CI/CD pipelines or test reporting tools.

### \`-v\` or \`--verbose\`

- **Usage**: Increases the verbosity of the test output.
- **Example**: \`pytest -v\`
- **Explanation**: Provides more detailed output about which tests are running and their results.

### \`-s\`

- **Usage**: Allows printing to the console from the test code.
- **Example**: \`pytest -s\`
- **Explanation**: Useful when you want to see output from print statements within your tests.

## Writing Tests

### Adding New Scenarios

1. **Create or Update a Feature File**: Add new scenarios in the appropriate \`.feature\` file under the \`features/\` directory.
2. **Implement Step Definitions**: Implement the corresponding step definitions in the relevant test script located in the \`tests/\` directory.

### Marking Tests

Use \`@pytest.mark.<marker>\` to tag your tests. Example:

\`\`\`python
@pytest.mark.regression
def test_some_feature():
    # Test code here
\`\`\`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or raise an Issue.

## License

This project is licensed under the MIT License.
