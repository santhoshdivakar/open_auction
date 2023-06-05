
import sqlalchemy

# create an orm model for auction table using sqlalchemy
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zipcode = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_modified = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    auctions = relationship("Auction", backref="user")
    bids = relationship("Bid", backref="user")

    def __init__(self, username, password, email, phone, address, city, state, zipcode, country, is_admin=False):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % (self.username)


# create an orm model for auction table using sqlalchemy which contains a foreign key to user table
class Auction(Base):
    __tablename__ = 'auction'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, default=datetime.datetime.utcnow)
    start_price = Column(Float, nullable=False)
    current_price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_modified = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    bids = relationship("Bid", backref="auction")

    def __init__(self, title, description, start_date, end_date, start_price, current_price, user_id):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.start_price = start_price
        self.current_price = current_price
        self.user_id = user_id

    def __repr__(self):
        return '<Auction %r>' % (self.title)