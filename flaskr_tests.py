import os
import fisher
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, fisher.app.config['DATABASE'] = tempfile.mkstemp()
        fisher.app.config['TESTING'] = True
        self.app = fisher.app.test_client()
        fisher.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(fisher.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()