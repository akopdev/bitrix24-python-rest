# Bitrix24 REST API for Python

Easy way to communicate with bitrix24 portal over REST without OAuth 2.0

## Description

Bitrix24 REST is an API wrapper for working with Bitrix24 REST API over webhooks.
No OAuth 2.0 required. It's easy to use and super lightweight, with minimal dependencies.

## Features

- Works with both cloud and on-premises versions of Bitrix24.
- Super easy to setup. No OAuth 2.0 infrastructure required.
- Built with data analysis in mind and fully compatible with Jupyter Notebook.
- Fetch paginated data at once without hassle.
- Works with large datasets and handles rate limits.

## Installation

```
pip install bitrix24-rest
```

## Quickstart

```python
from bitrix24 import Bitrix24

bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu')

print(bx24.callMethod('crm.product.list'))
```

In async mode:

```python
import asyncio
from bitrix24 import bitrix24

async def main():
    bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu')
    result = await bx24.callMethod('crm.product.list')
    print(result)

asyncio.run(main())
```

## Advanced usage

- [Using filters and additional parameters](docs/using-filters-and-additional-parameters.md)
- [Working with large datasets](docs/working-with-large-datasets.md)
- [Disabling certificate verification](docs/disabling-certificate-verification.md)

## Notes

List methods return all available items at once. For large collections of data use limits.

## Development

New contributors and pull requests are welcome. If you have any questions or suggestions, feel free to open an issue.

Code comes with makefile for easy code base management. You can check `make help` for more details.

```sh
make init install # to create a local virtual environment and install dependencies

make test # to run tests

make lint # to run linter
```

I suggest to use `make all` before committing your changes as it will run all the necessary checks.

## Support this project

You can support this project by starring ⭐, sharing 📤, and contributing. 

You can also support the author by buying him a coffee ☕. Click sponsor button on the top of the page.
