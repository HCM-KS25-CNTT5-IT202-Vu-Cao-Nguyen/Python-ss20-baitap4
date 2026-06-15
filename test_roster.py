import unittest

from main import calculate_actual_pay


class TestCalculateActualPay(unittest.TestCase):

    def test_active_player(self):

        player = {
            "salary": 5000,
            "status": "Active"
        }

        self.assertEqual(
            calculate_actual_pay(player),
            5000
        )

    def test_benched_player(self):

        player = {
            "salary": 6000,
            "status": "Benched"
        }

        self.assertEqual(
            calculate_actual_pay(player),
            3000
        )


if __name__ == "__main__":
    unittest.main()