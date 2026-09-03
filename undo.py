

class State:
    def __init__(self):
        self.actions = []
        self.current_action_index = -1

    def get_data(self):
        return ''.join(self.actions[:self.current_action_index + 1])

    def action(self, new_data):
        if self.current_action_index < len(self.actions) - 1:
            self.actions[self.current_action_index + 1] = new_data
        else:
            self.actions.append(new_data)
            self.current_action_index += 1
        return self

    def undo(self):
        if self.current_action_index > 0:
            self.current_action_index -= 1
        return self

    def redo(self):
        if self.current_action_index < len(self.actions) - 1:
            self.current_action_index += 1
        return self

state = State()
state.action("Hello").action(" myy").action(" name").action(" is").action(" John")
print(state.get_data())  # Output: "Hello World"

state.undo().undo().undo().undo()
print(state.get_data())  # Output: "Hello"

state.action(" my")

state.redo().redo().redo().redo()
print(state.get_data())  # Output: "Hello World"