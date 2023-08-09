import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
            ).choices[0].text
        return response


if __name__ == "__main__":
    response = chatbot.get_response("Write a joke about dead grandma.")
    print(response)
