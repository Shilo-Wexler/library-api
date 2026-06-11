# library-api
<br>
<br>
This system manages a server-side connection for a library.
The system creates a link to a database where the books, their current status, and subscriber information will be stored.
And also manages methods to conveniently receive the information through end points.

```
library-api
├── README.md
├── app
│   ├── database
│   │   ├── book_db.py
│   │   ├── connection_db.py
│   │   └── member_db.py
│   ├── logs
│   │   └── app.log
│   ├── main.py
│   └── routes
│       ├── book_routes.py
│       ├── member_routes.py
│       └── report_routes.py
└── requirements.txt
```
<br>

<br>

## SQL table structure


### 'books' table:

| field | explanation |
|  :---- | :--------- |
| `id` |   Master key |
| `title` | Book title maximum 50 characters | 
| `author` | Author's name, maximum 50 characters | 
| `genre` | Allowed values:  ​​Fiction, Non-Fiction, Science, History, Other. Values ​​are required -> Implemented as an ENUM |
| `is_available` | A borrowed book is represented by TRUE, the opposite of FALSE | 
| `borrowed_by_member_id` | Lender ID possible null| 



### 'members' table:

| field | explanation |
| ----- | :---- |
| `id` | Master key |
| `name` | Member, non-empty column, maximum 50 characters |
| `email` | Email address — unique, non-empty column |
| `is_active` | Is the member active — FALSE Cannot borrow a non-empty column |
| `total_borrows` |Total Borrowing count — increases by 1 for each question with a non-empty column |
<br>

## System rules
|  | case | rules|
| :---- | :---- | :---- |
| 1 | Add a book | Add a book |
| 2 | genre |Must be Fiction / Non-Fiction / Science / History / Other — any other value returns an error. Must be verified on both POST and PATCH |
| 3 | Add member | User sends title/author/genre — system adds `is_available=True`, `borrowed_by=NULL` |
| 4 | email | Must be unique — if already exists returns an error |
| 5 | Inactive member | If `is_active=False` — book cannot be borrowed |
| 6 | Book unavailable |You cannot borrow a book that is already borrowed (`is_available=False`) |
| 7 | Maximum books | A member cannot hold more than 3 books at a time. |
| 8 | Returning  book | A book can only be returned if it is lent to the same friend who is returning it |
<br>

##
## End Points

#### Books endpoints:

| Method | Endpoint | Description |
| :----- | :----- | :---- | 
| POST | `/books` | INSERT into the books table — `is_available=True`, `borrowed_by=NULL`|
| GET | `/books` | Returns a list of all books |
| GET | `/books/{id}` | Returns one book by ID or None |
| PATCH | `/books/{id}` | Updating submitted fields |
| PATCH | `/books/{id}/return/{member_id}` | Lending a book to a member |
| PATCH | `/books/{id}/borrow/{member_id}` | Returning a book from a member |


#### Reports endpoints:

| Method | Use | Description |
| :---- | :---- | :---- |
| GET | `/reports/summary` | General report |
| GET | `/reports/books-by-genre` | Books by genre | 
| GET | `/reports/top-member` | Returns the member with the highest `total_borrows` | 

## 

#### Members endpoints:


| Method | Use | Description |
| :---- | :---- | :---- |
| POST | `/members` | Add member |
| GET |  `/members` | Returns a list of all members |
| GET | `/members/{id}` | Returns one member by ID or None |
| PUT | `/members/{id}` | Updating submitted fields |
| PUT | `/members/{id}/deactivate` | Updating `is_active=False` |
| PUT | `/members/{id}/activate` | Updating `is_active=True` |
<br>


## System flow

- An http request is received through endpoints using fastapi
- Processed by functions that manage the database
- Data is updated and returned via fastapi


## Running instructions:

1 - Import command and create the container for database initialization:
```
docker run --name library-api \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=library_db \
  -p 3306:3306 \
  -d mysql:8
```
2 - Command to run the container:
```
docker exec -it library-api mysql -uroot -psecret
```
3 - Command to run an isolated environment for a project (venv):
```
python3 -m venv venv; source venv/bin/activate;
``` 
4 - Installing the libraries required for the project to run properly:
```
pip install -r requirements.txt  
```
5 - Run the project:
```
python3 app/main.py
```
