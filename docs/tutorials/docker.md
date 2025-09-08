# 🐳 Installing and Running the App with Docker

This guide will walk you through how to install the required Docker environment and run the app. The app is **Docker-runtime agnostic**, meaning it can run on various Docker runtimes, including Docker Desktop, Colima, or any compatible Docker engine.

## Install a container runtime

First, you’ll need to install Docker on your system. Below are some installation options depending on your preferences:

!!! quote ""
    === "Colima (macOS - Recommended)"

        If you'd prefer a lightweight, open-source alternative to Docker Desktop, you can install and use Colima. Colima runs Docker in a fast VM and is an excellent choice for those seeking a lightweight option. Follow these steps:

        1. Install Colima and Docker CLI using Homebrew:

            ```console
            $ brew install colima docker
            ```

        2. Start Colima to run a lightweight Docker engine:

            ```console
            $ colima start

            INFO[0001] starting colima
            INFO[0001] runtime: docker
            INFO[0003] starting ...                                  context=vm
            INFO[0015] provisioning ...                              context=docker
            INFO[0016] starting ...                                  context=docker
            INFO[0017] done
            ```

        ✅ Once Colima is started, you can use the Docker CLI (`docker`) just like you would with Docker Desktop !

        3. Check that the Docker daemon is running:

            ```console
            $ docker ps
            CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
            ```

        4. When you are done, stop the Docker VM by running:

            ```console
            $ colima stop
            ```

    === "Docker Desktop (macOS)"

        ⚠️ **Warning**: [Docker Desktop](https://docs.docker.com/desktop/) **requires a commercial license**. Make sure to be compliant before using.

        > **Docker Desktop terms**
        > Commercial use of Docker Desktop in larger enterprises (more than 250 employees or more than $10 million USD in annual revenue) requires a paid subscription.

        1. Download and install Docker Desktop from [Docker's official site](https://www.docker.com/products/docker-desktop).
        2. Launch the Docker Desktop app after installation.
        3. Check that the Docker daemon is running:

            ```console
            $ docker ps
            CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
            ```

??? quote "Pros and cons of each tool"
    |                      | **Colima**         | **Docker Desktop** |
    |----------------------|--------------------|--------------------|
    | **Pricing**          | ✅ Free            | ❌ Paid (for certain usage) |
    | **Resource Usage**   | ✅ Lightweight     | ❌ Heavy           |
    | **Interface**        | ❌ Console only    | ✅ GUI             |

## Build and Run the App in Docker

### 👾 Dev mode

This repo provides a ready-to-go setup to build and run a Docker image in interactive mode. This means that when you change a file in your IDE, the modifications are **directly applied** in the **running** Docker image. No rebuild is needed 🌟.

!!! warning ""
    ⚠️ This is for dev and debugging purpose **ONLY**. For production environments, refer to the [Prod mode](#prod-mode) example.

First lock your Python environment (needed by the Dockerfile) and set the necessary permissions. Then run the build and run script:

```bash
uv lock
chmod +x ./scripts/build_run_docker.sh
./scripts/build_run_docker.sh
```

Once the app starts, you should see the following output indicating that the FastAPI app is running:

```console
FastAPI   Starting development server 🚀

                Searching for package file structure from directories with __init__.py files
                Importing from /app

module   📁 app
                ├── 🐍 __init__.py
                └── 🐍 main.py

code     Importing the FastAPI app object from the module with the following code:

                from app.main import app

    app   Using import string: app.main:app

server   Server started at http://0.0.0.0:8000
server   Documentation at http://0.0.0.0:8000/docs
```

**Side-remarks:**

- The entire project is mounted as a volume (expect for the .venv folder), to avoid rebuilding the image.
- Providing arguments overwrites the default `fastapi dev` command (see the Dockerfile), and allows you to run with more control.
- The script kills the container when you leave it (because of `docker run --rm` flag).

### 🚀 Prod mode

In a **production** setup, it's best to build the image from scratch without relying on volume mounts:

```shell
export IMAGE_NAME="app-prod"
docker build -t "$IMAGE_NAME" .
docker run --rm --publish 8000:8000 --name "$IMAGE_NAME-container" --detach "$IMAGE_NAME" fastapi run
```

This time you get a truly self-packaged container, ready to be deployed:

```console
FastAPI   Starting production server 🚀
            ...
server   Server started at http://0.0.0.0:8000
server   Documentation at http://0.0.0.0:8000/docs
```

---

## FAQ

- **Fixing Docker Buildx Issues After Uninstalling Docker Desktop (macOS)**

    ```console
    $ docker buildx
    ERROR: BuildKit is enabled but the buildx component is missing or broken.
        Install the buildx component to build images with BuildKit:
    https://docs.docker.com/go/buildx/
    "docker run" requires at least 1 argument.
    See 'docker run --help'.

    Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
    ```

    ??? quote "Solution"

        By default, running `brew install docker` also installs `docker-buildx`, an extension of the Docker CLI that enables advanced build capabilities like multi-platform image builds.

        However, **uninstalling Docker Desktop can sometimes leave behind broken symlinks or outdated configurations**, which may cause `buildx` to misbehave. If you run into any `buildx`-related issues, follow these steps:

        **1. Install or Reinstall the `docker-buildx` plugin**

        ```bash
        brew install docker-buildx
        brew reinstall docker-buildx
        ```

        **2. Clean up old Docker Desktop configurations (if needed)**

        Sometimes residual configs interfere with plugin discovery. To ensure Docker recognizes the Buildx plugin, update your Docker CLI config:

        1. Open your Docker config file:

            ```bash
            nano ~/.docker/config.json
            ```

        2. Ensure the file includes:

            ```bash
            "cliPluginsExtraDirs": [
                "/opt/homebrew/lib/docker/cli-plugins"
            ]
            ```

        After this, you should be able to use `docker buildx` without issues. You can verify with:

        ```console
        $ docker buildx version
        github.com/docker/buildx v0.19.2-desktop.1 412cbb151f1be3f8a94dc4eb03cd1b67f261dec5
        ```
