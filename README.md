# SQL-Injection Demo
`index.html` contains a website that's prone to SQL Injection. 
SQL Injection is a code injection technique that can be used to access databases without authorization.

## Trying it for yourself
Run `api.py` and open `index.html` in a browser.

## How a SQL Query could look like
Let's say the website is dealing with a database with table `data` that stores in a field `data`. An example of checking
if the code `1X4Z25` is valid could look like this
```sql
select * from data where data='1X4Z25'
```
This sort of statement is extremely vulnerable.
## SQL Injection
The way we can test if a website is by using the escape character `'`. This sort of statement
could look like this: 
```sql
select * from data where data='''
```
which would throw the error `unrecognized token: "'''"`.
On a real website, this could throw something like `an unexpected error`.<br>
We can use SQL statements to complete the statement to always return something.<br>
By using a statement like `1=1` we can return everything in the database.
Such a statement could look like this.
```sql
select * from data where data='a' OR 1=1 OR 'b'
```
This would always validate us. By inserting `a' OR 1=1 OR 'b` in the text field this completes
the statement and returns a valid code.
The server can proceed to do other things with this code, even if you don't know what code you are using.<br>
<br>
SQL Injection also works if the data is numbers. For example, a sql statement accepting only numbers
could look like this.

```sql
select * from data where data=123456
```

Here, SQL Injection is a little bit more simple. We can test by using the escape character `'`,
and an example SQL Injection could look like this:
```sql
select * from data where data=123 OR 1=1
```
Here, by entering `123 OR 1=1`, we accomplish the same thing as last time.


