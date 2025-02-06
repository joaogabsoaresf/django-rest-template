import resend
from config import secrets
from django.template.loader import render_to_string

class ResendConnector:
    def __init__(self):
        self.api_key = secrets.RESEND_API_KEY
        self.from_email = "No-reply <no-reply@updates.joaosoares.dev>"

    def send_email(self, params: resend.Emails.SendParams):
        params["from"] = self.from_email
        return resend.Emails.send(params)

class OnboardingEmail(ResendConnector):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.template = "onboarding.html"

    def send(self):
        html_content = self.get_template()
        params = {
            "to": self.user.email,
            "subject": "Bem-vindo ao nosso app!",
            "html": html_content
        }
        return self.send_email(params)

    def get_template(self):
        context = {"user": self.user}
        return render_to_string(self.template, context)
