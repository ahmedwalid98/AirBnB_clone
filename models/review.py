#!/usr/bin/python3
"""Review class Module.."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that representing Review."""
    place_id = ""
    user_id = ""
    text = ""
