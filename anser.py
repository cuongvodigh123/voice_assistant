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
def handsome(query):
    if "đẹp trai" in query:
        answers = [
            "Tôi không biết, nhưng tôi cá bạn là người đẹp trai nhất thế giới.",
            "Bạn là nhất. Nhất bạn rồi",
            "Tôi không phải là người, tôi không thể đánh giá được độ đẹp trai của bạn."
        ]
        return random.choice(answers)
    if "xấu trai" in query:
        answers = [
            "có thể bạn không đẹp nhưng hãy tự tin với vẻ đẹp của mình.",
            "Bạn là nhất. Nhất bạn rồi. nên đừng lo lắng nhé",
            "Tôi không phải là người, đừng nó hỏi tôi ."
        ]
        return random.choice(answers)
    if "vẻ đẹp" in query:
        return "tôi không thể đánh giá được"