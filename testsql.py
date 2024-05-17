import random

# List of strings
strings = [
    '010100770004000', '000200010987000', '000200010986000', '010504050004000',
    '010102140007000', '010100720004000', '010101240004901', '010100950030000',
    '010101040016000', '010900490017000', '010900550001000', '010101180055903',
    '010101180054903', '010101180053903', '010101180008903', '010100990024000',
    '010401290001000', '010203220004000', '010204610001000', '010500240001000',
    '010201120007001', '010403310003000', '010200490010000'
]

# Function to generate the SQL UPDATE statement
def generate_update_statement(bio_number, some_id):
    update_stmt = f"UPDATE LxL4bMkc3EYQfTw3.users SET bio = '{bio_number}' WHERE id = {some_id};\n"
    return update_stmt

# Open a file for writing
with open('update_statements.sql', 'w') as file:
    # Iterate 100000 times to generate 100000 UPDATE statements
    for i in range(1, 100001):
        # Randomly select a string from the list
        random_string = random.choice(strings)

        # Use the loop index as the some_id value
        some_id = i

        # Generate the SQL UPDATE statement
        update_statement = generate_update_statement(random_string, some_id)

        # Write the UPDATE statement to the file
        file.write(update_statement)

print("SQL UPDATE statements have been saved to update_statements.sql")
