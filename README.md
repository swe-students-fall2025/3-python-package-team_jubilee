# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.


# Contribution
1. First, clone the repository into a workspace.
```Bash
git clone https://github.com/user/repository-name.git
```
2. Then, use pipenv to install all dependencies.
```Bash
pip install pipenv

pipenv install --dev
```

3. To build, run tests, or upload through twine, use pipenv to run our scripts.
```Bash
pipenv run test
pipenv run build
pipenv run upload
```