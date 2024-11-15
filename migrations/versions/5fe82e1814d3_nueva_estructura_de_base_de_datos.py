"""Nueva estructura de base de datos

Revision ID: 5fe82e1814d3
Revises: 
Create Date: 2024-11-13 09:35:56.024389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fe82e1814d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer_votes', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('answer_votes_answer_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('answer_votes_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'answers', ['answer_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('answers', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('question_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('answers_question_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('answers_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'questions', ['question_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('comments_user_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('comments_answer_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'answers', ['answer_id'], ['id'])

    with op.batch_alter_table('question_tags', schema=None) as batch_op:
        batch_op.drop_constraint('question_tags_question_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('question_tags_tag_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'questions', ['question_id'], ['id'])
        batch_op.create_foreign_key(None, 'tags', ['tag_id'], ['id'])

    with op.batch_alter_table('question_votes', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('question_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('question_votes_user_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('question_votes_question_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'questions', ['question_id'], ['id'])

    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('questions_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('questions_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('question_votes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('question_votes_question_id_fkey', 'questions', ['question_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('question_votes_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.alter_column('question_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('question_tags', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('question_tags_tag_id_fkey', 'tags', ['tag_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('question_tags_question_id_fkey', 'questions', ['question_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('comments_answer_id_fkey', 'answers', ['answer_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('comments_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('answers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('answers_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('answers_question_id_fkey', 'questions', ['question_id'], ['id'], ondelete='CASCADE')
        batch_op.alter_column('question_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('answer_votes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('answer_votes_user_id_fkey', 'users', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('answer_votes_answer_id_fkey', 'answers', ['answer_id'], ['id'], ondelete='CASCADE')
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###