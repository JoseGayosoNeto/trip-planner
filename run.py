from src.main.server.server import app
from src.models.settings.db_connection_handler import db_connection_handler
from src.ethereal_email_client.client.create_email import account_instance


if __name__ == "__main__":
    # Create connection with db before running app
    db_connection_handler.connect()
    account_instance.create_email()
    app.run(host="0.0.0.0", port=3000, debug=True)
