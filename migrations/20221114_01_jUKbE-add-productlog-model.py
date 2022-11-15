"""
Add ProductLog model
"""

from yoyo import step

__depends__ = {'20221113_02_5Cn3Y-add-product-model'}

steps = [
    step(
        """
        CREATE TABLE "product_log" (
            id UUID PRIMARY KEY,
            product_id UUID NOT NULL,
            ip_address VARCHAR NULL,
            created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
            FOREIGN KEY(product_id) REFERENCES product (id)
        )
        """,
        'DROP TABLE "product_log"',
    ),
]
