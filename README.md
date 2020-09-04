<!--- The following badges don't work because they're templated... uncomment when filled out
[![PyPI version](https://badge.fury.io/py/{{library_name}}.svg)](https://badge.fury.io/py/{{library_name}})
[![Build Status](https://travis-ci.{{com_or_org}}/{{travis_username}}/{{library_name}}.svg?branch=master)](https://travis-ci.{{com_or_org}}/{{travis_username}}/{{library_name}})
[![codecov](https://codecov.io/gh/{{codecov_username}}/{{library_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{codecov_username}}/{{library_name}})
[![Documentation Status](https://readthedocs.org/projects/{{library_name}}/badge/?version=latest)](https://{{library_name}}.readthedocs.io/en/latest/?badge=latest)
--->

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![black-girls-code](https://img.shields.io/badge/black%20girls-code-f64279.svg)](https://www.blackgirlscode.com/)


# Python Library Template
A github template for an up to date python library, featuring:
 - black style
 - sphinx docs with some examples and automatic build
 - pre-commit hooks
 - some example code for newer pythonistas
 - tox tests
 - travis ci + cd
 - code coverage

## Developer notes

**Documentation for use of the library is [here](https://{{library_name}}.readthedocs.io). You don't need to pay attention to the following unless you plan to develop {{library_name}} itself.**

### Getting started

1. Click 'use this template' to the top right, and away you go.
2. Search for `{{` in your new repository. Do search and replace for the various terms - it's obvious what they are, like replace `{{github_username}}` with your github username!
3. Set up the license you need in `LICENSE`.
4. If you need to deploy to pypi, you have to do the first deploy manually - travis can't do that for you. [See the packaging instructions](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi).

### Pre-Commit

You need to install pre-commit to get the hooks working. Do:
```
pip install pre-commit
pre-commit install
```

Once that's done, each time you make a commit, the following checks are made:

- valid github repo and files
- code style
- import order
- PEP8 compliance
- documentation build

Upon failure, the commit will halt. **Re-running the commit will automatically fix most issues** except:

- The flake8 checks... hopefully over time Black (which fixes most things automatically already) will negate need for it.
- You'll have to fix documentation yourself prior to a successful commit (there's no auto fix for that!!).

You can run pre-commit hooks without making a commit, too, like:
```
pre-commit run black --all-files
```
or
```
pre-commit run build-docs
```


### Contributing

- Please raise an issue on the board (or add your $0.02 to an existing issue) so the maintainers know
what's happening and can advise / steer you.

- Create a fork of {{library_name}}, undertake your changes on a new branch, named like *issue-84* or similar. To run tests and make commits,
you'll need to do something like:
```
git clone <your_forked_repo_address>    # fetches the repo to your local machine
cd {{library_name}}                     # move into the repo directory
pyenv virtualenv 3.6.9 myenv            # Makes a virtual environment for you to install the dev tools into. Use any python >= 3.6
pyend activate myenv                    # Activates the virtual environment so you don't screw up other installations
pip install -r requirements-dev.txt     # Installs the testing and code formatting utilities
pre-commit install                      # Installs the pre-commit code formatting hooks in the git repo
tox                                     # Runs the tests with coverage. NB you can also just set up pycharm or vscode to run these.
```

- Adopt a Test Driven Development approach to implementing new features or fixing bugs.

- Ask the `{{library_name}}` maintainers *where* to make your pull request. We'll create a version branch, according to the
roadmap, into which you can make your PR. We'll help review the changes and improve the PR.

- Once checks have passed, test coverage of the new code is >=95%, documentation is updated and the Review is passed, we'll merge into the version branch.

- Once all the roadmapped features for that version are done, we'll release.


### Release process

The process for creating a new release is as follows:

1. Check out a branch for the next version, called `vX.Y.Z`
2. Create a Pull Request into the `master` branch.
3. Undertake your changes, committing and pushing to branch `vX.Y.Z`
4. Ensure that documentation is updated to match changes, and increment the changelog. **Pull requests which do not update documentation will be refused.**
5. Ensure that test coverage is sufficient. **Pull requests that decrease test coverage will be refused.**
6. Ensure code meets style guidelines (pre-commit scripts and flake8 tests will fail otherwise)
7. Address Review Comments on the PR
8. Ensure the version in `setup.py` is correct and matches the branch version.
9. Merge to master. Successful test, doc build, flake8 and a new version number will automatically create the release on pypi.
10. Go to code > releases and create a new release on GitHub at the same SHA.


## Documents

### Building documents automatically

The documentation will build automatically in a pre-configured environment when you make a commit.

In fact, the way pre-commit works, you won't be allowed to make the commit unless the documentation builds,
this way we avoid getting broken documentation pushed to the main repository on any commit sha, so we can rely on
builds working.


### Building documents manually

**If you did need to build the documentation**

Install `doxgen`. On a mac, that's `brew install doxygen`; other systems may differ.

Install sphinx and other requirements for building the docs:
```
pip install -r docs/requirements.txt
```

Run the build process:
```
sphinx-build -b html docs/source docs/build
```
