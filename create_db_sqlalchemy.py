from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# 1. Create an engine that stores data in a address_alchemy.db file in the local directory
# The engine establishes a DBAPI connection to the database when a method like execute() or connect() is called
engine = create_engine('sqlite:///address_sqlalchemy.db')

# 2. Describe the model (i.e. the database tables and the classesmapped to those)

# Create the declarative base class. This stores a catlog of classes and mapped tables using the Declarative system
Base = declarative_base()

# Define the classes and tables
class Person(Base):
    __tablename__ = 'person'
    person_id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    address = relationship("Address")

    def __repr__(self):
        return "<Person(id='%s', first_name='%s', last name='%s')>" % (self.person_id, self.first_name, self.last_name)


class Address(Base):
    __tablename__ = 'address'
    address_id = Column(Integer, primary_key=True)
    street_name = Column(String(120))
    street_number = Column(String(6))
    post_code = Column(String(10))
    person_id = Column(Integer, ForeignKey('person.person_id'))

    def __repr__(self):
        return "<Address('%s', '%s', '%s)>" % (
            self.street_number, self.street_name, self.post_code)


# 3. Create all tables
Base.metadata.create_all(engine)

# 4. Create a session object to allow us to interact with the database
# Session class is defined using sessionmaker() – a configurable session factory method which is bound to the engine
# object created earlier.
Session = sessionmaker(bind=engine)
session = Session()

# 5. Create people objects then add to the database using the session object
p1 = Person(first_name='R2', last_name='D2')
session.add(p1)

session.add_all([
    Person(first_name='Metal', last_name='Mickey'),
    Person(first_name='Marvin', last_name='Paranoid-Android'),
    Person(first_name='K', last_name='9')]
)

# 4. Create address objects and add to the database
# Add a person and their address
et = Person(first_name='E.', last_name='T.')
# Address has to be a list even if there is only one address
et.address = [Address(street_number='1A', street_name='Brodo Asogi', post_code='')]
session.add(et)

# Add an address for an existing person
p2 = session.query(Person).filter_by(first_name='Metal').first()
p2.address = [Address(street_number='34', street_name='Wilberforce Street', post_code='B4 7ET')]

# 5. Commit the changes to the database
session.commit()

# 6. Close the session
session.close()