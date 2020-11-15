# Introduction

This repository contains the code from the book [Trading Evolved: Anyone Can Build Killer Trading Strategies In Python](https://www.followingthetrend.com/trading-evolved/) by Andreas F. Clenow.

# Why?

The goal of this repository is to make it easy for traders who are not software developers and/or Python programmers to get started experimenting with the code in the book. Readers do not have to worry about installing or patching zipline.
 
# Prerequisites

Download and install the following software:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. [VS Code](https://code.visualstudio.com/)

# Usage

1. Create an image for zipline.

   In a terminal, execute:
    ```bash
    docker build -t quantopian/zipline:trading_evolved https://github.com/hsm207/zipline.git#trading-evolved
    ```

2. Clone this project.

3. Open [devcontainer.json](./.devcontainer/devcontainer.json) and replace the value of `QUANDL_API_KEY` with your own API key (line 33).

4. In VS Code, open this project's root directory in a container defined by [Dockerfile](./Dockerfile).

5. When inside the container, execute `jupyter notebook --allow-root` to start viewing the notebooks.

6. To ingest the quandl bundle, refer to the [01_get_quandl_data](notebooks/00_Setup/01_get_quandl_data.ipynb) notebook,

# Useful Resources

* [VS Code: How To Open A Folder Inside A Container](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container)