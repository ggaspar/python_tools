class MementoPattern:
    class MementoException(Exception):
        pass

    def memento(self, **kwargs):
        if not hasattr(self, 'history'):
            self.history = list()
        old_values = {k: v for k, v in self.__dict__.items() if k != "history"}
        self.history.append(old_values)
        self._update_values(kwargs)

    def rollback(self):
        try:
            old_values = self.history.pop()
        except (IndexError, AttributeError):
            raise MementoPattern.MementoException("no historic to be re-used")
        self._update_values(old_values)

    def _update_values(self, new_values):
        for k, v in new_values.items():
            self.__dict__[k] = v