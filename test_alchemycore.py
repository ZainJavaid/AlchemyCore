# test_alchemycore.py
"""
Tests for AlchemyCore module.
"""

import unittest
from alchemycore import AlchemyCore

class TestAlchemyCore(unittest.TestCase):
    """Test cases for AlchemyCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlchemyCore()
        self.assertIsInstance(instance, AlchemyCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlchemyCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
