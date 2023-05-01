from core.db.session import session


def get_db():
    db = session()
    try:
        yield db
    except:
        db.close()
