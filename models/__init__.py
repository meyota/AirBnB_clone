#!/usr/bin/python3
"""package linker"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
