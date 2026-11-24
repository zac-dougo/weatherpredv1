## Summary

<!-- Briefly describe what changed and why. -->

## Checks

- [ ] Unit tests pass (`uv run --locked --no-dev --python 3.12 python -m unittest discover -s tests -v`)
- [ ] Lint, format, and type checks pass (`uv run --locked ruff check . && uv run --locked ruff format --check . && uv run --locked mypy src tests`)
- [ ] Documentation updates are reflected in `README.md` (if applicable)
