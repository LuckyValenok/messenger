from datetime import datetime

message_database = [
    {
        "id": 1,
        "chat_id": 1,
        "send_from": "user_1",
        "send_to": "user_2",
        "created_date": datetime(2023, 5, 1, 0, 36, 1),
        "text": "Hey!"
    },
    {
        "id": 2,
        "chat_id": 1,
        "send_from": "user_2",
        "send_to": "user_1",
        "created_date": datetime(2023, 5, 1, 0, 36, 2),
        "text": "Wow"
    },
]