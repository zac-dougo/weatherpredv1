<img src="assets/icon.svg" width="64" height="64" alt="">

# weatherpredv1

Created in [T3 Code](https://t3.codes).

## Run the tests and checks

```sh
uv run --locked --no-dev --python 3.12 python -m unittest discover -s tests -v
uv run --locked --python 3.12 ruff check .
uv run --locked --python 3.12 ruff format --check .
uv run --locked --python 3.12 mypy src tests
```
