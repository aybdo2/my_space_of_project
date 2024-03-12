#!/usr/bin/python3
"""
Define the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Present a user obfect with reective attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
