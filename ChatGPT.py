from openai import OpenAI

client = OpenAI(api_key='KEY_API')


def gpt(text):
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a bot assistant imitating a real person."},
            {'role': 'user', 'content': f'{text}'}
        ],
        temperature=0.5
    )

    english_text = completion.choices[0].message.content

    return english_text