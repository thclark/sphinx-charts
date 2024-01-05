FROM windpioneers/gdal-python:modest-heron-gdal-2.4.1-python-3.11-dev

# Tell zsh where you want to store history
#     We leave you to decide, but if you put this into a folder that's been mapped
#     into the container, then history will persist over container rebuilds :)
#
#     !!!IMPORTANT!!!
#     Make sure your .zsh_history file is NOT committed into your repository, as it can contain
#     sensitive information. So in this case, you should add
#         .devcontainer/.zsh_history
#     to your .gitignore file.
#
ENV HISTFILE="/workspaces/sphinx-charts/.devcontainer/.zsh_history"

# Install pre-commit for all users
RUN pip install pre-commit

# Install poetry
ENV POETRY_HOME=/home/vscode/.poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH "$POETRY_HOME/bin:$PATH"
RUN poetry config virtualenvs.create false

# Switch to vscode user
USER vscode

# Set the working directory
WORKDIR /workspaces/sphinx-charts
