
from position import Position

class Company:
    def __init__(self, root=None):
        self.root = root

    def build_from_json(self, file_path):
        pass
        

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