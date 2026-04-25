class Position:
    def __init__(self, first_name, second_name, name, parent=None):
        self.id = self.generate_id(first_name, second_name, name)
        self.first_name = first_name
        self.second_name = second_name
        self.name = name
        self.parent = parent
        self.subordinates = []

    @staticmethod
    def generate_id(first_name: str, second_name: str, position_name: str) -> str:
        if len(second_name) < 3:
            second_name += "0"
        elif len(first_name) < 3:
            first_name += "0"

        return f"{first_name[:2]}{second_name[:2]}{position_name[:2]}"

    def has_employee(self):
        return bool(self.first_name and self.second_name)

    def remove_employee(self):
        self.first_name = ""
        self.second_name = ""
        self.id = None

    def assign_employee(self, first_name, second_name):
        if self.has_employee():
            raise ValueError("Position is closed")
        
        self.name = first_name
        self.second_name = second_name
        self.id = self.generate_id(first_name, second_name)
        



