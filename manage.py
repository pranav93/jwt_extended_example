# USAGE
# python manage.py migratedb upgrade head
# python manage.py migratedb upgrade +number
# python manage.py migratedb downgrade -number
# python manage.py migratedb sync 0
# python manage.py migratedb drop 0
# python manage.py migratedb autogenerate 'message'
# python manage.py runserver [admin] [updatedb]
# python manage.py runserver [admin] [dropdb]
# python manage.py runserver [admin] [syncdb]

from shell import Shell
from app import create_app


def migrate_db(database_uri=None, migrate_jump=None, migrate_op=None):
    from models.configure import Model
    from alembic.config import Config, command
    from utils.helpers import config

    alembic_cfg = Config(file_='data/dev/alembic.ini')
    alembic_cfg.set_main_option("script_location", "models/alembic")
    alembic_cfg.set_main_option("sqlalchemy.url", database_uri if database_uri else config.SQLALCHEMY_DATABASE_URI)
    with Model.metadata.bind.begin() as connection:
        alembic_cfg.attributes['connection'] = connection
        alembic_fun = dict(
            upgrade=command.upgrade,
            downgrade=command.downgrade
        )

        if migrate_op == 'upgrade' or migrate_op == 'downgrade':
            alembic_fun[migrate_op](alembic_cfg, migrate_jump)
        elif migrate_op == 'drop':
            from onehop.models import Model
            Model.metadata.drop_all()

            connection = Model.metadata.bind.connect()
            connection.execute('drop table if exists alembic_version')
        elif migrate_op == 'sync':
            from onehop.models import Model
            Model.metadata.drop_all()

            connection = Model.metadata.bind.connect()
            connection.execute('drop table if exists alembic_version')
            migrate_op = 'upgrade'
            migrate_jump = '+1'
            alembic_fun[migrate_op](alembic_cfg, migrate_jump)
        elif migrate_op == 'autogenerate':
            command.revision(alembic_cfg, message=migrate_jump, autogenerate=True)


def migrate(args):
    database_uri = args.migrate_db_uri
    migrate_jump = args.migrate_jump
    migrate_op = args.migrate_op
    migrate_db(database_uri=database_uri, migrate_jump=migrate_jump, migrate_op=migrate_op)


def get_application(args=None):
    app = create_app()

    if args:
        if 'updatedb' in args.server_action:
            migrate_db(migrate_jump='head', migrate_op='upgrade')
        elif 'dropdb' in args.server_action:
            migrate_db(migrate_jump='0', migrate_op='drop')
        elif 'syncdb' in args.server_action:
            migrate_db(migrate_jump='0', migrate_op='sync')

        if 'admin' in args.server_action:
            from admin import admin
            admin.init_app(app)

    return app


def run_application(args=None):
    app = get_application(args=args)
    app.run('0.0.0.0', debug=True, threaded=True)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    # tell the parser that there will be subparsers
    subparsers = parser.add_subparsers(help="subparsers")

    # Add parsers to the object that was returned by `add_subparsers`
    parser_migrate = subparsers.add_parser('migratedb')

    # use that as you would any other argument parser
    parser_migrate.add_argument('migrate_op', type=str)
    parser_migrate.add_argument('migrate_jump', type=str)
    parser_migrate.add_argument('migrate_db_uri', nargs='?', type=str)

    # set_defaults is nice to call a function which is specific to each subparser
    parser_migrate.set_defaults(func=migrate)

    # repeat for our next sub-command
    parser_server = subparsers.add_parser('runserver')
    parser_server.add_argument('server_action', nargs='*', type=str)
    parser_server.set_defaults(func=run_application)

    parser_shell = subparsers.add_parser('shell')
    parser_shell.set_defaults(func=Shell())

    # parse the args
    args = parser.parse_args()
    args.func(args)  # args.func is the function that was set for the particular subparser
