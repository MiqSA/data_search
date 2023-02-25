import sys
sys.path.append('.')
import pytest
from sqlalchemy import text
from app.server import create_app, db

flag_delete_rows = False


@pytest.fixture(scope='module')
def client(delete_database_rows=flag_delete_rows):
    app = create_app('test')
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()
        
    yield testing_client
    
    if delete_database_rows:
        with app.app_context():
            session = db.session
            session.execute(text('DELETE FROM data'))
            session.commit()
