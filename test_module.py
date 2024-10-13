# test_module.py

import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot(self):
        """Test that the plot function returns a Matplotlib figure."""
        fig = draw_plot()
        self.assertIsNotNone(fig)

def run_tests():
    unittest.main(exit=False)
