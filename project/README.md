# {{project_name}}
{{project_description}}

## Usage

Write usage example here (will be tested by doccheck):
```python
>>> from {{project_name}} import add_two
>>> print(add_two(1,1))
2

```

## Requirements

- Python 3 (see pyproject.toml for specific version)

## Development

Setup dependencies in a virtual environment using [uv](https://docs.astral.sh/uv/):
```
uv sync
```

The prek Git hook is installed automatically when the project is generated.
Once project files are tracked by Git, run all configured hooks manually with:
```bash
uv run prek run --all-files
```

The virtual environment is activated automatically if you use [direnv](https://direnv.net/).

If not, activate the virtual environment (bash compatible on linux):
```bash
source .venv/bin/activate
```
Activate the virtual environment (powershell compatible on windows):
```bash
. .venv/Scripts/activate
```

You can run checks (linting, type checking, and tests) with `poe check`.

## License

TODO: figure out your license!
