"""Person and contact tables

Revision ID: baa191033433
Revises: 
Create Date: 2024-12-05 13:30:48.948578

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "baa191033433"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    contact_types = op.create_table(
        "contact_types",
        sa.Column("contact_type_id", sa.Integer(), nullable=False),
        sa.Column("contact_type_name", sa.String(), nullable=False),
        sa.Column("contact_type_engl_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("contact_type_id"),
    )
    op.create_table(
        "persons",
        sa.Column("person_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("person_name", sa.String(), nullable=False),
        sa.Column("person_birthday", sa.Date(), nullable=True),
        sa.Column("person_appeal", sa.String(), nullable=True),
        sa.Column("notes", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("person_id"),
    )
    op.create_table(
        "contacts",
        sa.Column("contact_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("person_id", sa.Integer(), nullable=False),
        sa.Column("contact_type_id", sa.Integer(), nullable=False),
        sa.Column("contact_text", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["contact_type_id"],
            ["contact_types.contact_type_id"],
        ),
        sa.ForeignKeyConstraint(
            ["person_id"],
            ["persons.person_id"],
        ),
        sa.PrimaryKeyConstraint("contact_id"),
    )
    # ### end Alembic commands ###

    op.bulk_insert(
        contact_types,
        [
            {
                "contact_type_id": 1,
                "contact_type_name": "Телефон",
                "contact_type_engl_name": "Phone",
            },
            {
                "contact_type_id": 2,
                "contact_type_name": "Электронная почта",
                "contact_type_engl_name": "Email",
            },
            {
                "contact_type_id": 3,
                "contact_type_name": "Телеграм",
                "contact_type_engl_name": "Telegram",
            },
            {
                "contact_type_id": 4,
                "contact_type_name": "ВК",
                "contact_type_engl_name": "VK",
            },
            {
                "contact_type_id": 5,
                "contact_type_name": "Фейсбук",
                "contact_type_engl_name": "Facebook",
            },
            {
                "contact_type_id": 6,
                "contact_type_name": "Адрес",
                "contact_type_engl_name": "Adress",
            },
        ],
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("contacts")
    op.drop_table("persons")
    op.drop_table("contact_types")
    # ### end Alembic commands ###
