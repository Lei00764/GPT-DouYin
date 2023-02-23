import openai

# OpenAI并没有提供一个公开的API来直接调用ChatGPT，但是您可以使用OpenAI的GPT-3 API来获得类似的结果.
# 密钥：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
# prompt：要说的话
# 返回 GPT-3 的答复
def generate_text(prompt):
    openai.api_key = "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"

    model_engine = "text-davinci-003"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    print(message)
    return message