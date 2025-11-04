"""
Flask CLI Command Extensions
"""
from service import app


######################################################################
# Command to force tables to be rebuilt
# Usage: flask db-create
######################################################################
@app.cli.command("db-create")
def db_create():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    # Import db lazily so importing this module does not import/initialize
    # the models package at module import time (prevents side-effects during tests).
    from service.models import db

    db.drop_all()
    db.create_all()
    db.session.commit()