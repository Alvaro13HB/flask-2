"""empty message

Revision ID: d3683dc1ce95
Revises: 
Create Date: 2024-10-11 08:17:13.288976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3683dc1ce95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carros',
    sa.Column('id_carro', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(length=50), nullable=True),
    sa.Column('modelo', sa.String(length=50), nullable=True),
    sa.Column('ano', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_carro')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carros')
    # ### end Alembic commands ###
