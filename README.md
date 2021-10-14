# pyDragonfly

[![PyPI version](https://badge.fury.io/py/pydragonfly.svg)](https://badge.fury.io/py/pydragonfly)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/pydragonfly.svg)](https://pypi.python.org/pypi/pydragonfly/)

Robust Python **SDK** and **Command Line Client** for interacting with Certego's [Dragonfly](https://dragonfly.certego.net/) service's API.

## Features

- Easy one-time configuration with self documented help and hints along the way.

## Installation

```bash
$ pip3 install pydragonfly
```

For development/testing, `pip3 install pydragonfly[dev]`

## Quickstart

### As a library / SDK

```python
from pydragonfly import Dragonfly
df = Dragonfly("<your_api_key>")
```

For more comprehensive documentation, please see https://pydragonfly.readthedocs.io/.

## Changelog

View [CHANGELOG.md](https://github.com/certego/pydragonfly/blob/master/.github/CHANGELOG.md).

## FAQ

#### Generate API token

You need a valid API token to interact with the Dragonfly server.
Head on over to https://dragonfly.certego.net/me/sessions and click on the "Generate +" button.
