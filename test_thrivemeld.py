# test_thrivemeld.py
"""
Tests for ThriveMeld module.
"""

import unittest
from thrivemeld import ThriveMeld

class TestThriveMeld(unittest.TestCase):
    """Test cases for ThriveMeld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThriveMeld()
        self.assertIsInstance(instance, ThriveMeld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThriveMeld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
