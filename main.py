import openai,os,local


def setup():
    os.environ["OPENAI_API_KEY"] = local.API_KEY


setup()

openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = "こんにちは、私の名前は"
model = "gpt-3.5-turbo"
response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=5
        ) 
print(response.choices[0].text)
