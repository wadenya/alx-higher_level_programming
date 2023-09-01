0x11. Python - Network #1

## What is `urllib`?

`urllib` is like a toolkit provided by Python to allow you to access content from the internet. Imagine you're at a library and want to read a book. Instead of walking to the shelf to pick it up yourself, you ask a librarian to get it for you. Here, `urllib` is like that librarian.

## How to fetch internet resources with `urllib`:

```python
import urllib.request

# This is the address of the book (or web page) you want to fetch.
url = "https://www.example.com"

# This line asks the librarian (`urllib`) to get the book for you.
response = urllib.request.urlopen(url)

# This line reads the content of the book.
data = response.read()
```

## Decoding `urllib` Body Response:

Now, let's assume that the book (`data`) the librarian brought you is written in a language that you can't understand (it's in bytes). You need to translate (or "decode") it to a language you know (like English, represented as text in programming):

```python
decoded_data = data.decode('utf-8')
```

## What is `requests`?

`requests` is another, more modern librarian, who is more efficient and user-friendly than the previous one (`urllib`). This librarian is so cool that they even understand if the book is written in a special format like JSON and can hand it to you in a way that's easier to understand.

## Using `requests`:

Before you can use this cool librarian, you need to hire (or "install") them:

```bash
pip install requests
```

## Making HTTP GET Request with `requests`:

Imagine you just want to see (or "GET") a book:

```python
import requests

response = requests.get("https://www.example.com")
print(response.text)
```

This tells the librarian, "Hey, can you show me the content of this web page?" And then it prints out what the librarian brings back.

## Making HTTP POST/PUT/etc. Request with `requests`:

Now, sometimes you want to do more than just "see" a book. Maybe you want to add (or "POST") a note inside it or replace (or "PUT") a page.

- **POST** (Adding a note):

```python
data_to_post = {"message": "Hello, world!"}
response = requests.post("https://www.example.com/notebook", data=data_to_post)
print(response.text)
```

- **PUT** (Replacing a page):

```python
data_to_put = {"page": "This is the new content for the page."}
response = requests.put("https://www.example.com/page", data=data_to_put)
print(response.text)
```

## Fetching JSON Resources:

Sometimes, websites give back information in a structured format called JSON. It's like if the librarian handed you a well-organized index card rather than a whole book.

```python
response = requests.get("https://api.example.com/data")
json_data = response.json()
print(json_data)
```

## Manipulating Data:

Now, once you've got the book or index card, you might want to do things with it.

For example, if you got a list of books:

```python
books = [{"title": "Harry Potter", "author": "J.K. Rowling"}, {"title": "Lord of the Rings", "author": "J.R.R. Tolkien"}]

for book in books:
    print(book['title'])
```

Here, you're just printing the title of each book in the list.

Remember, fetching and manipulating data can be a lot like dealing with books in a library. You decide what you want, ask the librarian (`urllib` or `requests`) to get it for you, and then work with what they bring back!
