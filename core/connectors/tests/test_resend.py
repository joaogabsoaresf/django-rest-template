import pytest
from unittest.mock import patch
from connectors.resend import ResendConnector, OnboardingEmail
from misc.fixtures.user import mock_user

@pytest.fixture
def resend_connector():
    return ResendConnector()

@pytest.fixture
def onboarding_email(mock_user):
    return OnboardingEmail(mock_user)

@patch("resend.Emails.send")
def test_send_email(mock_send, resend_connector):
    """Test if send_email correctly sends an email."""
    mock_send.return_value = {"id": "test-email-id"}
    
    params = {"to": "test@example.com", "subject": "Test", "html": "<p>Hello</p>"}
    response = resend_connector.send_email(params)

    mock_send.assert_called_once()
    assert response == {"id": "test-email-id"}

@patch("resend.Emails.send")
def test_onboarding_email_send(mock_send, onboarding_email):
    """Test onboarding email sends correctly."""
    mock_send.return_value = {"id": "onboarding-email-id"}

    response = onboarding_email.send()

    mock_send.assert_called_once()
    assert response == {"id": "onboarding-email-id"}