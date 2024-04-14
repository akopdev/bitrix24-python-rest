# Using filters and additional parameters

Define filters and additional parameters in any order using keyword arguments.

```python
bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu')

await bx24.callMethod('crm.deal.list',
                order={'STAGE_ID': 'ASC'},
                filter={'>PROBABILITY': 50},
                select=['ID', 'TITLE', 'STAGE_ID', 'PROBABILITY'])
```

You also can pass filters as a dictionary, similar to the original Bitrix24 API:

````python

payload = {
    'order': {'STAGE_ID': 'ASC'},
    'filter': {'>PROBABILITY': 50},
    'select': ['ID', 'TITLE', 'STAGE_ID', 'PROBABILITY']
}

await bx24.callMethod('crm.deal.list', payload)

````
