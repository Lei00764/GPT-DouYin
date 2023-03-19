import openai
import json

# prompt: 要说的话
# return: GPT-3.5 (即CHAT-GPT) 的答复
def generate_text(prompt):
    # 从 JSON 文件中读取数据
    with open('api.json') as f:
        data = json.load(f)
    # 获取 API URL
    api = data['api']
    openai.api_key = api

    resp = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=120 # 回复的最大字符数（大概）
    )
    content = resp['choices'][0]['message']['content']
    content = content.replace('\n', '')
    return content.strip()

print(generate_text("请列举5点软件工程专业的优点"))