# CLI

Run all datascience commands.

**Usage**:

```console
$ [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--verbose / --no-verbose`: [default: no-verbose]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `run`: Run cmd line entry point, e.g.
* `data`: Manages data flow.
* `model`: Manages model training and predictions.

## `run`

Run cmd line entry point, e.g. useful to start pipelines.

**Usage**:

```console
$ run [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `data`

Manages data flow.

**Usage**:

```console
$ data [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `download`: Download data from somewhere in the cloud.
* `build`: Build a dataset based on downloaded data...
* `delete`: Delete a dataset.

### `data download`

Download data from somewhere in the cloud.

**Usage**:

```console
$ data download [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `data build`

Build a dataset based on downloaded data that is useful for the model.

**Usage**:

```console
$ data build [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `data delete`

Delete a dataset.

**Usage**:

```console
$ data delete [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `model`

Manages model training and predictions.

**Usage**:

```console
$ model [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `train`: Perform model training.
* `predict`: Perform predictions.

### `model train`

Perform model training.

**Usage**:

```console
$ model train [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `model predict`

Perform predictions.

**Usage**:

```console
$ model predict [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
