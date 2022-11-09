"""
Add User model
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE "user" (
            id UUID PRIMARY KEY,
            name VARCHAR(90) NOT NULL,
            type VARCHAR(25) NOT NULL,
            is_active BOOLEAN DEFAULT True,
            created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL
        )
        """,
        'DROP TABLE "user"',
    ),
]
