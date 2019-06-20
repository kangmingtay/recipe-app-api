from unittest.mock import patch # allows us to simulate the database not being available

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Tests waiting for db when db is available"""
        # Overwrite behaviour of the connection handler
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)  # replaces the behaviour of time.sleep, don' want to slow down test execution
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True] # raise OperationalError 5 times, return on the last try
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
