import random
def check_weather(query):
    if "đẹp trời" in query:
        answers = [
            "Tôi không biết, nhưng trời hôm nay khá tốt.",
            "Tôi không đánh giá được thời tiết bên ngoài, nhưng trong phòng thì rất dễ chịu.",
            "Tôi không phải là người, tôi không thể đánh giá được thời tiết."
        ]
        return random.choice(answers)
    if "tồi tệ" in query:
        answers = [
            "Tôi không biết, nhưng hy vọng bạn sẽ có một ngày tốt hơn.",
            "Tôi không thể cảm nhận được cảm giác của bạn, nhưng tôi luôn ở đây để giúp bạn nếu cần.",
            "Hy vọng mọi chuyện sẽ tốt hơn trong những ngày tiếp theo."
        ]
        return random.choice(answers)