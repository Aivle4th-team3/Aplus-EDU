from config.settings import chatbot
import numpy as np


def talk_to_bot(message, history):
    # 챗봇에 기억 저장소 역할로 보내줄 메시지
    selected_messages = []
    # 러프한 길이 제한
    LEN_LIMIT = 10000

    # 메시지 임베딩 벡터화
    user_message_embedded = chatbot.get_embedding(message)
    if history:
        embedded_history = np.array(
            [msg.user_message_embedded for msg in history])
        # 코사인 유사도 비교
        # 각 임베딩된 벡터의 크기가 1이므로 분모 생략
        cosine_similarity = np.dot(embedded_history, user_message_embedded)
        # 유사도 높은 순서로 선택하려고 뒤집음
        descent_idx = np.argsort(cosine_similarity)[::-1]
        len_count = 0
        for idx in descent_idx:
            if len_count < LEN_LIMIT:
                current_message = history[idx.item()]
                selected_messages.append(
                    (current_message.user_message, current_message.bot_message))
                len_count += (len(current_message.user_message) +
                              len(current_message.bot_message))

    # 현재 메시지와 기억 저장소 역할의 메시지를 전송
    answer = chatbot.chat(message, selected_messages)

    bot_message_embedded=chatbot.get_embedding(answer)

    return answer, user_message_embedded, bot_message_embedded
