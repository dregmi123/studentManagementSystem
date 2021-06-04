"""grades table

Revision ID: 1727bc06f1a6
Revises: 879492fffc61
Create Date: 2021-05-24 19:44:21.898918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1727bc06f1a6'
down_revision = '879492fffc61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grade', 'grade_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grade', sa.Column('grade_number', sa.VARCHAR(length=12), nullable=False))
    # ### end Alembic commands ###