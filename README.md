# upycode

micropython sample code

## upload script

```sh
mpremote cp <board>/<filename>.py :main.py
```

## develop

```sh
poetry install --sync --with <board>
poetry run inv fmt
poetry run inv lint
```
