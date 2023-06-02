import sqlite3
from models import Size

def get_all_sizes(query_params):
    """Using SQL database to get all styles"""
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
            z.id,
            z.carets,
            z.price         
        FROM Size z
        {sort_by}
        """
    db_cursor.execute(sql_to_execute)

    sizes = []

    dataset = db_cursor.fetchall()

    for row in dataset:

        size = Size(row['id'], row['carets'], row['price'])

        sizes.append(size.__dict__)

    return sizes


# Function with a single parameter
def get_single_size(id):
    """New single order request for SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            z.id,
            z.size,
            z.price         
        FROM Size z
        WHERE z.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        size = Size(data['id'], data['size'], data['price'], )

        return size.__dict__
