"""Database connection management"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        # Get database URL from environment
        self.database_url = os.getenv('DATABASE_URL')
        
        if not self.database_url:
            user = os.getenv('POSTGRES_USER', 'university_admin')
            password = os.getenv('POSTGRES_PASSWORD', 'SecurePass123!')
            host = os.getenv('POSTGRES_HOST', 'localhost')
            port = os.getenv('POSTGRES_PORT', '5432')
            db = os.getenv('POSTGRES_DB', 'university_db')
            self.database_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
        
        # Create database engine
        self.engine = create_engine(
            self.database_url,
            echo=False,  # Set to True to see SQL queries
            pool_size=5,
            max_overflow=10
        )
        
        # Create session factory
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False
        )
    
    def get_session(self):
        """Get a database session"""
        return self.SessionLocal()

# Singleton instance
db = Database()