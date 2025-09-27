def show_messages(messages):
    """向列表中的每个用户发出简单的问候"""
    for message in messages:
        msg = f"Hello, What are you doing now？{message.title()}"
        print(msg)
    user_messages = ["I'm reading", "I'm studying", "I'm playing on my phone"]
    show_messages(user_messages)
