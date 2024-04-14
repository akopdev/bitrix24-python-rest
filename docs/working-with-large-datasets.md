# Working with large datasets

Fetching large datasets can be a problem. Bitrix24 REST API has a limit of 50 items per request and a rate limiter 
that can block your requests if you exceed the limit. 

This library has a built-in feature to handle large datasets without any hassle. 
It will automatically detect if the dataset is paginated and fetch all the data at once.

Also, all requests are made concurrently, which means you can fetch data faster and with low resource usage.

However, if you for any reason want to disable this feature, you can do so by setting the `fetch_all_pages` parameter to `False`.


```python

bx24 = Bitrix24('https://example.bitrix24.com/rest/1/33olqeits4avuyqu', fetch_all_pages=False)

# `page1` will contain only the first page of the dataset
page1 = await bx24.callMethod('crm.deal.list')

# fetch next page
page2 = await bx24.callMethod('crm.deal.list', start=50)
```

In this mode, you will need to handle pagination manually.
