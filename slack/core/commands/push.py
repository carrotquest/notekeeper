from abc import abstractmethod, ABC

from core.entities.note import UserId, Note
from core.interfaces import IdentifiedCommand


class PushHandler(ABC):
    """
    Push command executor interface
    """

    @abstractmethod
    def handle_push(self, command: 'Push') -> Note:
        pass


class Push(IdentifiedCommand[PushHandler]):
    """Add note to list"""

    text: str  # Note text

    def __init__(self, user_id: UserId, text: str):
        super().__init__(user_id)
        self.text = text

    def handle(self, handler: PushHandler) -> Note:
        return handler.handle_push(self)
