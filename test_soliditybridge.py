# test_soliditybridge.py
"""
Tests for SolidityBridge module.
"""

import unittest
from soliditybridge import SolidityBridge

class TestSolidityBridge(unittest.TestCase):
    """Test cases for SolidityBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityBridge()
        self.assertIsInstance(instance, SolidityBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
