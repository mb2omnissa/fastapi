# from fastapi import FastAPI
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from app.main import app
#
# from app.database import get_db, Base
# import pytest
#
#
#
# SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:Wysescale@localhost:5432/fastapi_test"
#
#
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Base.metadata.create_all(bind=engine)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# # def override_get_db():
# #     print("Using test database:", SQLALCHEMY_DATABASE_URI)
# #     db = TestingSessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()
#
# # try:
# #     app.dependency_overrides[get_db] = override_get_db
# #     print("Successfully set dependency override for get_db.")
# # except BaseException as e:
# #     print("Exception on override_get_db:", e)
# #     print("Details:", type(e).__name__, "-", e)
#
#
# @pytest.fixture()
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# @pytest.fixture()
# def client(session):
#     """
#     Provides a test client for FastAPI app and ensures database cleanup after tests.
#     """
#     # Yield the test client for use in tests
#     # command.upgrade("head")
#     # with TestClient(app) as test_client:
#     #     yield test_client
#     #     # command.downgrade(test_client)
#     def override_get_db():
#         print("Using test database:", SQLALCHEMY_DATABASE_URI)
#         try:
#             yield session
#         finally:
#             session.close()
#
#     app.dependency_overrides[get_db] = override_get_db
#     yield TestClient(app)
#
#
#     # Drop tables after tests are complete
#     # Base.metadata.drop_all(bind=engine)
