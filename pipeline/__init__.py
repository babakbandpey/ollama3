"""
The pipeline module provides a high-level interface for running a sequence of
"""

from .pipeline import Pipeline
from .chatbot import Chatbot
from .text_rag import TextRAG
from .web_rag import WebRAG
from .python_rag import PythonRAG
from .config import OPENAI_API_KEY

# Package-level variables
__version__ = '0.1.0'
__author__ = 'Babak Bandpey <bb@cocode.dk>'
__all__ = [
    'Pipeline',
    'Retrieval',
    'Chatbot',
    'TextRAG',
    'WebRAG',
    'PythonRAG',
    'OPENAI_API_KEY'
]