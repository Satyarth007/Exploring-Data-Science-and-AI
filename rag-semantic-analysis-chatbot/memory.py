chat_memory = []

def store(user, bot):
    chat_memory.append((user, bot))

def get_context():
    return "\n".join([f"User: {u}\nBot: {b}" for u,b in chat_memory[-3:]])
