# Linting

## Linting: Black

Also formats

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

## Linting: mypy

Checks types

```bash
mypy .
mypy . --strict
```

```json
{
  "python.linting.mypyEnabled": true,
  "python.linting.mypyArgs": [
    "--follow-imports=silent",
    "--show-column-numbers",
    "--strict"
  ]
}
```

## Linting: prospector
Useful extra hints, like unused imports

```bash
prospector
```

```json
{
  "python.linting.prospector": true
}
```

## Linting: pydocstyle
Helps with documentation

```bash
pydocstyle
```

```json
{
  "python.linting.pydocstyle": true
}
```