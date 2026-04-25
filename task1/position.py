class Position:
    def __init__(self, first_name: str, second_name: str, name: str, parent=None, new_id=None):
        self.first_name = first_name
        self.second_name = second_name
        self.name = name
        self.parent = parent
        self.subordinates = []

        if new_id:
            self.id = new_id
        else:
            self.id = self.generate_id(first_name, second_name, name)

    @staticmethod
    def generate_id(first_name: str, second_name: str, name: str) -> str:
        if len(first_name) < 3:
            first_name += "0"

        if len(second_name) < 3:
            second_name += "0"

        return f"{first_name[:3]}{second_name[:3]}{name[:3]}".lower()

    def has_employee(self) -> bool:
        return bool(self.first_name and self.second_name)

    def remove_employee(self):
        self.first_name = ""
        self.second_name = ""
        self.id = None

    def assign_employee(self, first_name: str, second_name: str):
        if self.has_employee():
            raise ValueError("Position closed")

        self.first_name = first_name
        self.second_name = second_name
        self.id = self.generate_id(first_name, second_name, self.name)