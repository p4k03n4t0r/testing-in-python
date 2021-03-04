# Linting

## Linting: Black

```bash
https://pypi.org/project/black/
black --check .
black .
```

```json
{
  "editor.formatOnSave": true,
  "python.formatting.provider": "black"
}
```

```bash
mypy .
mypy . --strict
```

## Static Code Analysis: mypy

```json
{
  "python.linting.mypyEnabled": true,
  "python.linting.mypyArgs": [
    "--follow-imports=silent",
    "--show-column-numbers",
    "--strict"
  ],
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": false
}
```
