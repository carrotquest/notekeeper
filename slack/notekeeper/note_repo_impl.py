from typing import List

from core.interfaces import NoteRepo
from core.entities import UserId, Note
from notekeeper.models import NoteModel


class NoteRepoImpl(NoteRepo):
    def create(self, user_id: UserId, text: str) -> Note:
        note_obj = NoteModel.objects.create(user_id=user_id, text=text)
        return note_obj.to_note()

    def get_last(self, user_id: UserId, n: int) -> List[Note]:
        return list(map(lambda note: note.to_note(),
                        NoteModel.objects
                        .filter(user_id=user_id)
                        .order_by('-created_at')[:n]
                        )
                    )
