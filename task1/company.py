import json
from position import Position

class Company:
    def __init__(self, root=None):
        self.root = root

    def build_from_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        position_by_name = {}

        for items in data:
            position = Position(
                items["first_name"], items["last_name"], items["name"],
                items["id"]
            )

            if not items["parent"]:
                self.root = position
                continue

            position_by_name[position.name] = position

        for items in data:
            parent_name = items["parent"]

            cur_pos = position_by_name[items["name"]]
            parent_pos = position_by_name[items["parent_name"]]
            cur_pos.parent = parent_pos
            parent_pos.subordinates.append(cur_pos)

    def find_position_by_name(self, position_name):
        pass

    def find_position_by_employee(self, first_name, second_name):
        pass

    def add_position(self, position_name, parent_position_name, first_name="", second_name=""):
        pass

    def print_all_positions(self):
        pass

    def close_position(self, position_name):
        pass

    def remove_employee(self, first_name, second_name):
        pass

    def assign_employee_to_free_position(self, position_name, first_name, second_name):
        pass

    def move_position(self, position_name, new_parent_name):
        pass


company1 = Company()

company1.build_from_json("data.json")