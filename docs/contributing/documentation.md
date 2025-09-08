# Documentation

The documentation process relies on [**Mkdocs**](https://www.mkdocs.org) with the [**Material theme**](https://squidfunk.github.io/mkdocs-material/getting-started/)  which allows to write markdown styled documentation.

We chose mkdocs as it is lighter and easier to configure than Sphinx (and in many cases more than enough).

## Build doc

To preview your documentation in real-time while editing, run:

```bash
uv sync --extra docs
mkdocs serve
```

Some usefuls commands:

```console
mkdocs new [dir-name]`  # create a new project.
mkdocs serve`           # starts local server with the documentation.
mkdocs build`           # builds documentation.
mkdocs -h`              # display help message.
```

## Deploy

The nice part is that the documentation can be hosted on the repository Github page with a single command:

```bash
mkdocs gh-deploy
```

## Change style

To adapt the doc style to your style guidelines, change:

1. **the colors** in the `docs/stylesheets/extra.css` file
2. **the logo and favicon** in the `docs/assets/images/` folder
