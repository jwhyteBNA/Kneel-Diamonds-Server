import sqlite3
from models import Metal

def get_all_metals(query_params):
    """Using SQL database to get all metals"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        sort_options = {
            "price": "price"
        }

        for param in query_params:
            qs_key, qs_value = param.split('=')
            if qs_key == "_sortBy" and qs_value in sort_options:
                sort_by = f" ORDER BY {sort_options[qs_value]}"

        sql_to_execute = f""" SELECT
            m.id,
            m.metal,
            m.price         
        FROM Metal m
        {sort_by}
        """

    db_cursor.execute(sql_to_execute)

    metals = []

    dataset = db_cursor.fetchall()

    for row in dataset:

        metal = Metal(row['id'], row['metal'], row['price'])

        metals.append(metal.__dict__)

    return metals

def get_single_metal(id):
    """New single metal request for SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM "Metal" m
        WHERE m.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        metal = Metal(data['id'], data['metal'], data['price'], )

        return metal.__dict__

def update_metal(id, new_metal):
    """UPDATE in SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metal
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'],  id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

# def get_all_metals():
#     """Sends all metals."""
#     return METALS

# # Function with a single parameter
# def get_single_metal(id):
#     """To get single metal."""
#     # Variable to hold the found metal, if it exists
#     requested_metal = None

#     # Iterate the METALS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for metal in METALS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if metal["id"] == id:
#             requested_metal = metal

#     return requested_metal
