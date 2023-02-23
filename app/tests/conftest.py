import sys
sys.path.append('.')
import pytest
from sqlalchemy import text
from app.server import create_app, db


@pytest.fixture(scope='module')
def client():
    app = create_app('test')
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()
        
    yield testing_client
        
    with app.app_context():
        session = db.session
        session.execute(text('DELETE FROM data'))
        session.commit()
