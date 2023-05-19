#!/usr/bin/python3
"""
creates new instance of FileStorage as storage
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
