# Disabling certificate verification

By default, the library verifies SSL certificates. If you want to disable this behavior, you can set `safe` parameter to `False` in the `Bitrix24` class.

This tells Python's underlying SSL handling to accept the server's certificate even if it's expired or invalid.

```python
bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu', safe=False)

await bx24.callMethod('crm.deal.list')
```

## Important Consideration 

Disabling SSL certificate verification undermines the security of HTTPS by making your application vulnerable to man-in-the-middle attacks. 

It should only be used in controlled environments, such as development or testing, where security is not a concern.

