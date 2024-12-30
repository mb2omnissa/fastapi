import sys
import os

# Add the parent directory to sys.path so that SAJAPI can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.config import settings
# Now try importing
from app.models import Base
print("Import succeeded!")

print(f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}")