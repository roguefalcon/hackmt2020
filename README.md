# Charity Toy Tracker 9000
Toys for Tots, Angel Tree, Holiday Heros, are all charities that help underprivileged kids have a
great Christmas with Toys and other more practical items (clothes, shoes, coats, etc.).

The software available to large scale organizations is often too expensive to purchase or much
too difficult to administer and deploy by the “small” charities. If a group wants to help less than
1,000 children. Some older legacy systems require physical paper forms (gasp).

Our software will be basic but have a few key features to enable smaller charities to assist in
these functions.

## Technologies
This is a Python Flask App that uses a bootstrap frontend and using Vue javascript framework.
We are using SQLite as the backend.

## Installation

Run the following commands:
```Bash
`pip3 install -r requirements.txt`
`python3 app.py`

## Database

Please run below command to set up database:
Children Database:
`python3 load_db.py` if you have error, please run this line again
Donor Database:
`python3 donor_register_db`
`python3 rea_db.py`
