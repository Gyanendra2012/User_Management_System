from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User, UserStatus

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    #  Add create() Method
    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        
        return user
    
    # Find User by Email
    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        
        return self.db.scalar(statement)
    
    # Find User by ID
    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        
        return self.db.scalar(statement)
    
    # Find User by Username
    def get_by_username(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        
        return self.db.scalar(statement)
        
    # Update User (Partial)
    def update(self, user: User, update_data: dict) -> User:
        for field, value in update_data.items():
            setattr(user, field, value)
            
        self.db.flush()
        self.db.refresh(user)
        
        return user
    
    # User Deactivation: soft deactivation istead of physically deleting the user
    def deactivate(self, user: User) -> User:
        user.status = UserStatus.INACTIVE
        
        self.db.flush()
        self.db.refresh(user)
        
        return user
    
    
    
    