class history():
    def execute(self, cls):
        self.get_complete_history(cls.history_stack)

    def get_complete_history(self, stack):
        for i in reversed(stack):
            print(i)