import json
#from collections import deque
from position import Position

class Company:
    def __init__(self, root=None):
        self.root = root

    def build_from_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        positions_by_name = {}

        for item in data:
            position = Position(
                first_name=item["first_name"],
                second_name=item["second_name"],
                name=item["name"],
                new_id=item["id"]
            )

            positions_by_name[position.name] = position

            if item["parent"] is None:
                self.root = position

        for item in data:
            parent_name = item["parent"]

            if parent_name is not None:
                current_position = positions_by_name[item["name"]]
                parent_position = positions_by_name[parent_name]

                current_position.parent = parent_position
                parent_position.subordinates.append(current_position)

    def find_position(self, attr, value):
        def dfs(node):
            if node is None:
                return None

            if getattr(node, attr) == value:
                return node

            for sub in node.subordinates:
                found = dfs(sub)
                if found:
                    return found

            return None

        return dfs(self.root)    

    def add_position(self, position_name, parent_position_name, first_name="", second_name=""):
        parent_node = self.find_position("name", parent_position_name)
        
        new_position = Position(
            first_name, second_name, 
            position_name, parent_node
        )

        parent_node.subordinates.append(new_position)

    def print_all_positions(self):
        def printer(cur_node: Position, counter: int):
            if cur_node is None:
                return
            
            print("---"*counter + f"{cur_node.name}({cur_node.first_name + ' ' + cur_node.second_name})")

            for node in cur_node.subordinates:
                printer(node, counter+1)
        printer(self.root, 0)

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
company1.print_all_positions()