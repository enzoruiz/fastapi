"""
Add User model
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE "myuser" (
            id UUID PRIMARY KEY,
            username VARCHAR NOT NULL,
            password VARCHAR NOT NULL,
            name VARCHAR(90) NOT NULL,
            role VARCHAR(25) NOT NULL,
            is_active BOOLEAN DEFAULT True,
            created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL
        )
        """,
        'DROP TABLE "myuser"',
    ),
]
