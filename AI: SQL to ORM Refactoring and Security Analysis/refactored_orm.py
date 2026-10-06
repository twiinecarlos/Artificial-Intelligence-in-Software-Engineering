import os
from sqlalchemy import String, URL, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)

engine = create_engine(URL.create(
    "mysql+mysqlconnector",
    username=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"],
    host=os.getenv("DB_HOST", "localhost"), database=os.environ["DB_NAME"]))

def _check(*vals):
    if not all(v and v.strip() for v in vals):
        raise ValueError("Missing input.")

def _find(s, username):
    return s.scalar(select(User).where(User.username == username))

def create_user(username, email):
    _check(username, email)
    try:
        with Session(engine, expire_on_commit=False) as s, s.begin():
            s.add(user := User(username=username, email=email))
        return user
    except IntegrityError:
        raise ValueError("Username or email exists.") from None

def get_user_by_username(username):
    with Session(engine) as s: return _find(s, username)

def update_user_email(username, new_email):
    _check(username, new_email)
    with Session(engine) as s, s.begin():
        if user := _find(s, username): user.email = new_email
        return user is not None

def delete_user(username):
    with Session(engine) as s, s.begin():
        if user := _find(s, username): s.delete(user)
        return user is not None

def list_users():
    with Session(engine) as s: return list(s.scalars(select(User)))

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    create_user("carlos", "carlos@example.com")
    print(get_user_by_username("carlos").email)
