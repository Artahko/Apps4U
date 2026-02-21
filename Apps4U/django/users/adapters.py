from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)

        # Save Google data automatically
        user.first_name = data.get("given_name", "")
        user.last_name = data.get("family_name", "")
        user.email = data.get("email", "")

        return user
