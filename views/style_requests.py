import sqlite3
from models import Style

def get_all_styles(query_params):
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
            s.id,
            s.style,
            s.price         
        FROM Style s
        {sort_by}
        """
    db_cursor.execute(sql_to_execute)

    styles = []

    dataset = db_cursor.fetchall()

    for row in dataset:

        style = Style(row['id'], row['style'], row['price'])

        styles.append(style.__dict__)

    return styles

# Function with a single parameter
def get_single_style(id):
    """New single style request for SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            s.id,
            s.style,
            s.price
        FROM Style s
        WHERE s.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        style = Style(data['id'], data['style'], data['price'], )

        return style.__dict__
