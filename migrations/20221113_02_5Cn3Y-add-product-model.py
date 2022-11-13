"""
Add Product model
"""

from yoyo import step

__depends__ = {'20221113_01_WJpjr-add-user-model'}

steps = [
    step(
        """
        CREATE TABLE "product" (
            id UUID PRIMARY KEY,
            name VARCHAR(90) NOT NULL,
            sku VARCHAR(25) NOT NULL,
            price FLOAT NOT NULL,
            brand VARCHAR(25) NOT NULL,
            is_active BOOLEAN DEFAULT True,
            created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL
        )
        """,
        'DROP TABLE "product"',
    ),
]
