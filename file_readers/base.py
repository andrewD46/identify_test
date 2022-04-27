from abc import ABC


class AbstractFileReader(ABC):
    def __init__(self, file: str):
        self.file = file

    def to_dataframe(self):
        raise NotImplemented
