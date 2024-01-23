from config.settings import chatbot
import numpy as np


def talk_to_bot(message, user_messages):
    # history로 사용될 메시지
    selected_messages = []
    # 러프한 길이 제한
    LEN_LIMIT = 10000

    user_message_embedded = chatbot.get_embedding(message)
    if user_messages:
        embedded_user_vectors = np.array([msg.user_message_embedded for msg in user_messages])
        descent_idx = np.argsort(np.dot(embedded_user_vectors, user_message_embedded))[::-1]
        len_count = 0
        for idx in descent_idx:
            if len_count < LEN_LIMIT:
                current_message = user_messages[idx.item()]
                selected_messages.append(
                    (current_message.user_message, current_message.bot_message))
                len_count += (len(current_message.user_message) +
                              len(current_message.bot_message))

    answer = chatbot.chat(message, selected_messages)

    bot_message_embedded=chatbot.get_embedding(answer)

    return answer, user_message_embedded, bot_message_embedded
