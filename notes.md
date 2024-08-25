
## Flask DB commands

flask db init
    > Initializes the migrations directory.
flask db migrate -m "message"
    > Generates a new migration script based on model changes.
flask db upgrade
    > Applies the migrations to the database.
flask db downgrade
    > Rolls back the last migration applied.
flask db current
    > Shows the current migration version applied to the database.
flask db stamp <revision>
    > Stamps the database with a specific revision without running migrations.
flask db migrate --autogenerate -m "message"
    > Automatically generates a migration script based on detected changes.
flask db downgrade <revision>
    > Rolls back the database to a specific revision.
flask db history
    > Displays the history of all applied migrations.
flask db merge <revision1> <revision2> -m "message"
    > Merges two branches in the migration history.

