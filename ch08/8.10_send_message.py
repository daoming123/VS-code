<<<<<<< HEAD
def show_messages(messages):
    """向列表中的每个用户发出简单的问候"""
    for message in messages:
        msg = f"Hello, What are you doing now？{message.title()}"
        print(msg)


def send_messages(messages, sent_messages):
    """将每条消息都打印出来并移到一个名为sent_messages 的列表中"""
    while messages:
        current_messages = messages.pop(0)
        print(f"sending messages: {current_messages}")
        sent_messages.append(current_messages)


user_messages = ["I'm reading", "I'm studying", "I'm playing on my phone"]
sent_messages = []

print("== 原列表内容 ==")
show_messages(user_messages)

print("\n== 发送并转移消息 ==")
send_messages(user_messages, sent_messages)

print("\n== 发送后，两边列表检查 ==")
print("user_messages:\n", user_messages)

print("sent_messages:\n", sent_messages)
=======
def show_messages(messages):
    """向列表中的每个用户发出简单的问候"""
    for message in messages:
        msg = f"Hello, What are you doing now？{message.title()}"
        print(msg)


def send_messages(messages, sent_messages):
    """将每条消息都打印出来并移到一个名为sent_messages 的列表中"""
    while messages:
        current_messages = messages.pop(0)
        print(f"sending messages: {current_messages}")
        sent_messages.append(current_messages)


user_messages = ["I'm reading", "I'm studying", "I'm playing on my phone"]
sent_messages = []

print("== 原列表内容 ==")
show_messages(user_messages)

print("\n== 发送并转移消息 ==")
send_messages(user_messages, sent_messages)

print("\n== 发送后，两边列表检查 ==")
print("user_messages:\n", user_messages)

print("sent_messages:\n", sent_messages)
>>>>>>> ddb9f76865614855e9dbead36ef2c8d652b156f5
