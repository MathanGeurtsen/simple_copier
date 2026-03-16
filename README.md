# Simple copier template
This is a simple copier template for python projects with the following features:
 - simple setup
 - standard package structure
 - dev environment and CI included
 - template updates via `copier update`

 It is compatible with both windows and linux.

## Usage

Ensure you have git and uv installed. See [uv](https://docs.astral.sh/uv/) for its install instructions.

You can make a new project based on this repository:
```bash
uvx copier copy --trust https://github.com/MathanGeurtsen/simple_copier my_project
```

Once copier has ran, activate the new virtual environment with:

bash compatible on linux:
```bash
cd my_project && source .venv/bin/activate
```
powershell compatible on windows:
```bash
cd my_project; . .venv/Scripts/activate
```

You can run checks (linting, type checking, and tests) with `poe check`. 

### Updating an existing project

To pull in template updates to an already generated project:
```bash
cd my_project
copier update --trust
```

## Requirements

- copier
- uv
- git

## License

This project is licensed under the MIT License - see the LICENSE file for details.
