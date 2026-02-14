import datetime


def format_chat_for_download(messages, model_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"OmniChat Export\nModel: {model_name}\nDate: {timestamp}\n{'-'*30}\n\n"
    chat_content = ""
    for msg in messages:
        role = msg["role"].capitalize()
        chat_content += f"{role}: {msg['content']}\n\n"
    return header + chat_content


def count_tokens(text):
    return len(text.split()) * 1.3


def calculate_cost(tokens, model_name):
    costs = {
        "gpt-4o": 0.005,
        "gpt-4o-mini": 0.00015,
        "gpt-4-turbo": 0.01,
        "gpt-3.5-turbo": 0.001,
    }
    rate = costs.get(model_name, 0.001)
    return (tokens / 1000) * rate


def generate_chat_title(messages):
    if not messages:
        return "New Chat"
    first_msg = messages[0]["content"]
    title = " ".join(first_msg.split()[:4])
    return title.strip() or "Chat Export"
