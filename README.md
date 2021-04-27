* Create User Endpoint http://127.0.0.1:8000/
* List User Endpoint http://127.0.0.1:8000/list-users/
* Update User Endpoint http://127.0.0.1:8000/update-user/1/
* Update Product Info http://127.0.0.1:8000/update-product-info/


To import product info data for a specific user

```
./manage.py importdata user744@example.com ./product_list_with_emails.csv
```