class Commands:

    commands : dict[str, function] = {}

    def add_func(self, func : function, name: str):
        self.commands[name] = func
        pass

    def get(self, name):
        return self.commands[name]
        pass

    def run_func(self, name: str):
        self.commands[name]

    def get_command_name(self, id: int):
        return list(self.commands.keys())[id]
