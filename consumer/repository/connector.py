from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Factory:

    def __init__(self, db_uri):

        if not hasattr(self, "engine"):
            self.engine = create_engine(db_uri)
            self.session = sessionmaker(bind=self.engine)()

    def create(self, model):

        self.session.add(model)
        self.session.commit()

    
    def get_session(self):
        return self.session()
    
    