from alembic import command
from alembic.config import Config

print("Alembic command module imported successfully")

# Load the Alembic configuration (replace with your path)
alembic_cfg = Config("alembic.ini")

# Run migrations (test)
command.upgrade(alembic_cfg, "head")
