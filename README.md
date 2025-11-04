# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# Animal Say
Make animals say things with moods in ASCII art!

- AVAILABLE ANIMALS: cow, dog, cat, sheep
- AVAILABLE MOODS: happy, sad, neutral, angry, surprised

USAGE:

```python
import animalsay
print(animalsay.dog("Hello! I'm a happy dog!", mood="happy"))
```

EXAMPLE OUTPUT:

```
Hello! I'm a happy dog!
      \
       \   / \__
          (    ∩\\__
          /         O
         /   (_____/
        /_____/   U
```

# Team Members
- [Jasmine Zhu](https://github.com/jasminezjr)
- [Grace He](https://github.com/gracehe04)
- [Vaishnavi Suresh](https://github.com/vaishnavi-suresh)
- [Chengqi Li](https://github.com/lichengqi617)
- [Krystal Lin](https://github.com/krystalll-0)


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