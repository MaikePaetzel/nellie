"""A module for the abstract definitions of dialogue manager as used in
ReTiCo."""


class DialogueAct():
    """A Dialogue act containing an act, concepts and optionally a confidence
    score."""

    def __init__(self, act, concepts=None):
        self.act = act
        if concepts:
            self.concepts = concepts
        else:
            self.concepts = {}

    def __repr__(self):
        return "%s - %s" % (self.act, self.concepts)


class AbstractDialogueManager():
    """An abstract dialogue manager.

    This dialogue manager may be used turn based by returning a dialogue act and
    concepts each time a dialogue act from an interlocutor is introduced, or
    the dialogue manager may be able to produce multiple outputs without getting
    response from the interlocutor.
    """

    def process_act(self, act, concepts):
        """Process the given act and concepts.

        This method creates a DialogueAct object with the given act and concepts
        and calls the process_dialogue_act method.

        Args:
            act (str): The act that should be processed as a string.
            concepts (dict): The concepts as key-value pairs.
        """
        da = DialogueAct(act, concepts)
        self.process_dialogue_act(da)

    def process_dialogue_act(self, dialogue_act):
        """Prcoess an act received from an interlocutor.

        Args:
            dialogue_act (DialogueAct): The dialogue_act that should be
            processed.
        """
        raise NotImplementedError

    def next_act(self):
        """Return the next dialogue act and concepts as determined by the
        current state of the dialogue manager.

        The current state includes the last processed act.

        Returns:
            (str, dict): A tuple containing the dialogue act as a string, and a
            dictionary containing all concepts in the form of key-value-pairs.
        """
        raise NotImplementedError
