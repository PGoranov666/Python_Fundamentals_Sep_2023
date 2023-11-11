class ParkingSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, license_plate):
        if username in self.users:
            print(f"ERROR: already registered with plate number {self.users[username]}")
        else:
            self.users[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    def unregister_user(self, username):
        if username not in self.users:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del self.users[username]

    def print_registered_users(self):
        for username, license_plate in self.users.items():
            print(f"{username} => {license_plate}")


def main():
    n = int(input())
    parking_system = ParkingSystem()

    for _ in range(n):
        command = input().split()
        action = command[0]

        if action == "register":
            username, license_plate = command[1], command[2]
            parking_system.register_user(username, license_plate)
        elif action == "unregister":
            username = command[1]
            parking_system.unregister_user(username)

    parking_system.print_registered_users()


if __name__ == "__main__":
    main()
