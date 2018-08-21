
import json

from retico.core.abstract import AbstractConsumingModule
from retico.core.dialogue.common import DispatchableActIU, DialogueActIU

class DialogueActRecorderModule(AbstractConsumingModule):
    """A module that writes dispatched dialogue acts to file."""

    @staticmethod
    def name():
        return "Dialogue Act Recorder Module"

    @staticmethod
    def description():
        return "A module that writes dialogue acts into a file."

    @staticmethod
    def input_ius():
        return [DialogueActIU, DispatchableActIU]

    def __init__(self, filename, separator="\t", **kwargs):
        super().__init__(**kwargs)
        self.filename = filename
        self.separator = separator
        self.txt_file = None

    def setup(self):
        self.txt_file = open(self.filename, "w")

    def shutdown(self):
        if self.txt_file:
            self.txt_file.close()
            self.txt_file = None

    def process_iu(self, input_iu):
        if self.txt_file:
            self.txt_file.write(str(input_iu.creator))
            self.txt_file.write(self.separator)
            self.txt_file.write(str(input_iu.created_at))
            self.txt_file.write(self.separator)
            self.txt_file.write(input_iu.act)
            self.txt_file.write(self.separator)
            self.txt_file.write(json.dumps(input_iu.concepts))
            if isinstance(input_iu, DispatchableActIU):
                self.txt_file.write(self.separator)
                self.txt_file.write(str(input_iu.dispatch))
            self.txt_file.write("\n")
