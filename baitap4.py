import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s"
)


def calculate_actual_pay(player_dict):
    """
    Tính lương thực nhận của tuyển thủ.
    Active  -> 100% lương
    Benched -> 50% lương
    """

    try:
        salary = player_dict["salary"]
        status = player_dict["status"]

        if salary <= 0:
            raise ValueError("Salary must be greater than 0.")

        if status == "Active":
            return salary

        if status == "Benched":
            return salary * 0.5

        return 0

    except KeyError as error:
        logging.error(f"Missing key: {error}")
        raise

    except ValueError as error:
        logging.error(error)
        raise


def display_roster(roster_list):
    """
    Hiển thị danh sách tuyển thủ.
    """

    if not roster_list:
        print("Roster is empty.")
        return

    print("\n===== ROSTER LIST =====")

    for player in roster_list:
        print(
            f"ID: {player.get('player_id', 'N/A')} | "
            f"Name: {player.get('name', 'N/A')} | "
            f"Role: {player.get('role', 'N/A')} | "
            f"Status: {player.get('status', 'Unknown')}"
        )


def sign_player(roster_list):
    """
    Thêm tuyển thủ mới.
    """

    try:
        player_id = input("Player ID: ").strip().upper()

        for player in roster_list:
            if player["player_id"] == player_id:
                raise ValueError("Player ID already exists.")

        name = input("Player Name: ").strip()
        role = input("Role: ").strip()
        salary = float(input("Salary: "))
        status = input("Status (Active/Benched): ").strip()

        if salary <= 0:
            raise ValueError("Salary must be greater than 0.")

        new_player = {
            "player_id": player_id,
            "name": name,
            "role": role,
            "salary": salary,
            "status": status
        }

        roster_list.append(new_player)

        logging.info(f"Added player: {player_id}")
        print("Player added successfully.")

    except ValueError as error:
        logging.error(error)
        print(f"ERROR: {error}")


def update_player_status(roster_list):
    """
    Cập nhật trạng thái tuyển thủ.
    """

    try:
        player_id = input("Enter player ID: ").strip().upper()

        for player in roster_list:

            if player["player_id"] == player_id:

                new_status = input(
                    "New status (Active/Benched): "
                ).strip()

                if new_status not in ["Active", "Benched"]:
                    raise ValueError("Invalid status.")

                player["status"] = new_status

                logging.info(
                    f"Updated status of {player_id} to {new_status}"
                )

                print("Update successful.")
                return

        raise ValueError("Player not found.")

    except ValueError as error:
        logging.error(error)
        print(f"ERROR: {error}")


def generate_payroll_report(roster_list):
    """
    Tạo báo cáo quỹ lương.
    """

    total_payroll = 0

    print("\n===== PAYROLL REPORT =====")

    for player in roster_list:

        try:
            actual_pay = calculate_actual_pay(player)

            print(
                f"{player['name']} | "
                f"{player['status']} | "
                f"Actual Pay: {actual_pay}"
            )

            total_payroll += actual_pay

        except (KeyError, ValueError) as error:
            logging.error(error)

    print("-" * 40)
    print(f"TOTAL PAYROLL: {total_payroll}")


def main():

    roster_list = [
        {
            "player_id": "P001",
            "name": "Levi",
            "role": "Jungle",
            "salary": 5000,
            "status": "Active"
        },
        {
            "player_id": "P002",
            "name": "Kati",
            "role": "Mid",
            "salary": 4000,
            "status": "Benched"
        }
    ]

    while True:

        print("\n===== ROSTER MANAGEMENT =====")
        print("1. Display Roster")
        print("2. Sign Player")
        print("3. Update Player Status")
        print("4. Payroll Report")
        print("5. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            display_roster(roster_list)

        elif choice == "2":
            sign_player(roster_list)

        elif choice == "3":
            update_player_status(roster_list)

        elif choice == "4":
            generate_payroll_report(roster_list)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
