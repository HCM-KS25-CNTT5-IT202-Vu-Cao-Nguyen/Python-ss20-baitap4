mport unittest

from main import calculate_actual_pay


class TestCalculateActualPay(unittest.TestCase):

    def test_active_player_should_receive_full_salary(self):
        """
        Active -> nhận 100% lương
        """

        player = {
            "player_id": "P001",
            "name": "Levi",
            "salary": 5000,
            "status": "Active"
        }

        expected_result = 5000

        actual_result = calculate_actual_pay(player)

        self.assertEqual(expected_result, actual_result)

    def test_benched_player_should_receive_half_salary(self):
        """
        Benched -> nhận 50% lương
        """

        player = {
            "player_id": "P002",
            "name": "Kati",
            "salary": 4000,
            "status": "Benched"
        }

        expected_result = 2000

        actual_result = calculate_actual_pay(player)

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
