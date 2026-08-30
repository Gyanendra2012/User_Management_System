from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User, UserStatus
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate


# Service use same database session created at session.py
class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)


    def register_user(self, data: UserCreate):
        # Check whether email is already registered
        existing_user = self.user_repository.get_by_email(data.email)
        
        if existing_user:
            raise ValueError("Email already registered")
        
        # Check whether username is already registered
        existing_user = self.user_repository.get_by_username(data.username)
        
        if existing_user:
            raise ValueError("Username already registered")
        
        # Hash plaintext password
        password_hash = hash_password(data.password)
        
        # Create User ORM object
        user = User(
            username = data.username,
            email=data.email,
            password_hash=password_hash,
            full_name=data.full_name,
            mobile=data.mobile,
            status=UserStatus.ACTIVE,
            email_verified=True,
        )
        
        # Connect Service to Repository and Add Transaction Handling
        try:
            # Persist user through repository
            created_user = self.user_repository.create(user)
            
            # Commit transaction
            self.db.commit()
        
            return created_user

        except Exception:
            # Rollback transaction if anything fails
            self.db.rollback()
            raise

           
        
