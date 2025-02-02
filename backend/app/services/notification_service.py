# backend/app/services/notification_service.py
def send_notification(event: str, data: dict):
    """
    Envoie une notification via un système externe ou un workflow.
    Pour cet exemple, nous nous contentons de logger l'événement.
    """
    print(f"Notification - Event: {event}, Data: {data}")
    # Vous pouvez intégrer ici des appels à des webhooks, n8n, etc.
