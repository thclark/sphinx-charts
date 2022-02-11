# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.187.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Option] Install Node.js
ARG INSTALL_NODE="true"
ARG NODE_VERSION="lts/*"
RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install Oh-My-Zsh shell for development
#    - af-magic theme (because it looks closest to the github theme I use in VSCode, change to your preference)
#    - git, ssh and command history searching enabled (add more plugins as you wish)
#    - command history file mapped into the .devcontainer folder to enable reuse between container builds
ENV HISTFILE="/workspace/.devcontainer/.zsh_history"
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)" -- \
    -t af-magic \
    -p git -p ssh-agent -p 'history-substring-search' \
    -a 'bindkey "\$terminfo[kcuu1]" history-substring-search-up' \
    -a 'bindkey "\$terminfo[kcud1]" history-substring-search-down'

# The non-root user defined in the devcontainer.json file needs write permission to /usr/local/src
# in order for poetry to install git dependencies (this is where it clones them).
# Other installers (e.g. the austin profiling tool) will also require access to this directory
RUN mkdir -p /usr/local && chown -R vscode /usr/local

# Install austin for code profiling
RUN cd /usr/local/src && \
    git clone --depth=1 https://github.com/P403n1x87/austin.git && \
    cd /usr/local/src/austin && \
    autoreconf --install && \
    ./configure && \
    make && \
    make install

# Make sure that if you install requests, it can find the Certificate Authority bundle.
# Overcomes this issue: https://github.com/python-poetry/poetry/issues/1012
RUN export PYTHON_VERSION=`python -c 'import sys; print("{0}.{1}".format(*sys.version_info[:2]))'` && \
    mkdir -p /home/vscode/.local/lib/python${PYTHON_VERSION}/site-packages/certifi/ && \
    ln -s $(python -c "import certifi; print(certifi.where())") /home/vscode/.local/lib/python${PYTHON_VERSION}/site-packages/certifi/cacert.pem

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1


# Install poetry, cache poetry dependencies
#
#    Poetry usage in docker: https://stackoverflow.com/a/54763270/3556110
#    Caching package downloads with buildkit: https://pythonspeed.com/articles/docker-cache-pip-downloads/
#    Using pipx for python development utilities: https://github.com/microsoft/vscode-dev-containers/blob/main/containers/python-3/README.md#installing-or-updating-python-utilities
#    Notes:
#     - pipx just doesn't get it right. The dependencies end up not being found by the linter, so we fall back to the recommended way of installing poetry
#     - Poetry and dependencies can be agony, particularly surrounding the permissions of the vscode user, so we don't get hyper opinionated here
#     - I just can't get dependency caches working correctly with the vscode user across all platforms (permissions stuff)
#
USER vscode
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH "/home/vscode/.poetry/bin:$PATH"
RUN poetry config virtualenvs.create false
