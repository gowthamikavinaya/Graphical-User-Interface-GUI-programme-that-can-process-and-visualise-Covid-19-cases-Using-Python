import unittest
import gui
from datetime import datetime


class TestGui(unittest.TestCase):
    
    def tearDown(self):
        self.app.destroy()
    
    def test_startup(self):
        self.app = gui.run()
        self.app.mainloop()
        title = self.app.winfo_toplevel().title()
        expected = 'Covid19 and Stop & Search Information Centre'
        self.assertEqual(title, expected)
        
        



if __name__ == "__main__":
    unittest.main()