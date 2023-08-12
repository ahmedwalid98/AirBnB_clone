#!/usr/bin/python3
"""
    User class Module.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class that representing User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
