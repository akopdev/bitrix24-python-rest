# Bitrix24 REST API for Python

Easy way to communicate with bitrix24 portal over REST without OAuth 2.0

## Description

Bitrix24 REST is a simple API wrapper for working with Bitrix24
REST API over webhooks.

## Features

- Works both with cloud and on-premises versions of bitrix24, much more
- Super easy for setting up. No OAuth implemetation required
- Compatible with latests Bitrix24 REST API

## Requirements
- Python 2.6+ or 3.2+
- requests

## Installation
```
pip install bitrix24-rest
```

## Quickstart

```python
from bitrix24 import *

bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu')

print(bx24.callMethod('crm.product.list'))
```

## Advanced usage

You can define filters and additional parameters in any order:

```python
bx24.callMethod('crm.deal.list',
                order={'STAGE_ID': 'ASC'},
                filter={'>PROBABILITY': 50},
                select=['ID', 'TITLE', 'STAGE_ID', 'PROBABILITY'])
```

Catch the server error with exception:

```python
try:
    bx24.callMethod('tasks.task.add', fields={'TITLE': 'task for test', 'RESPONSIBLE_ID': 1})
except BitrixError as message:
    print(message)
```

## Notes
List methods return all available items at once. For large collections
of data use limits.

## Tests

```
python -m unittest discover
```

## Author

Akop Kesheshyan - <akop.kesheshyan@icloud.com>

New contributers and pull requests are welcome.