# The HTTP Library

Implement client and server to:

- Store book information (auth required)
- Search books by title and author (auth optional)
- Bookings of books (auth required)
- Limit book creation to admin users only


## Store book information

User can _create_ a book by `POST`ing to a http API using
a CLI client:

    python library_client.py store --title "The songlines" --author "Chatwin" --user pippo --password pass

The client uses the standard output to inform the user about operation completion and/or errors.


## Search books by title and author

User can _search_ the online catalogue by `GET`ing using an HTTP API:

    python library_client.py search --term "Montalbano"


## Booking

User can book an item using the CLI.

	python library_client.py book --title "The songlines" --user pippo --password pass

The client warns the user if the book is not available
or if it has already been booked by the calling user.

1) free -> book it
2) someone else has booked it
3) the calling user has already booked it
4) the book is not found


## Authentication

All authenticated calls might fail if the provided credentials are incorrect.


## Permission levels

There are two types of users:

- Staff: can create books
- non-staff: can only book books
