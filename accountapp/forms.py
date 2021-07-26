from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # username 필드 disable 처리하도록 커스터마이징
        self.fields['username'].disabled = True