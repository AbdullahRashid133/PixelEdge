# test_pixeledge.py
"""
Tests for PixelEdge module.
"""

import unittest
from pixeledge import PixelEdge

class TestPixelEdge(unittest.TestCase):
    """Test cases for PixelEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelEdge()
        self.assertIsInstance(instance, PixelEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
