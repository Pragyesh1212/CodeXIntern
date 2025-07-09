from monsterapi import client
import requests
import webbrowser
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Say the Propmt to generate the image:')
    audio = r.listen(source, timeout=5, phrase_time_limit=10)

    t = r.recognize_google(audio, language='en-US')
    print("Prompt:", t)

api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjhlM2M3NDA4ZjFmNDhhNjkwYzlmMjUwMjZhYjdiZDVmIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMDdUMDA6MzE6NTYuMjQ0NjcxIn0.B0pFX7n1xHNJCQov5RypePQZWwDo9FFlqQr4btFq0Nc'

monster_client=client(api_key)

prompt=("Prompt to generate image:",t)

model='txt2img'
input_data={
    'prompt':f'{prompt}',
    'negprompt':'bad anatomy',
    'samples':1,
    'steps':50,
    'aspect_ratio':'square',
    'guidance_scale':7.5,
    'seed':2424    
}
result=monster_client.generate(model,input_data)
# print(result['output'])
img_url=result['output'][0]
file_name="generated_image.jpg"

#download
response=requests.get(img_url)
if response.status_code==200:
    with open(file_name,'wb') as file:
        file.write(response.content)
    print("Image Dowloaded")
    
    #open the image
    webbrowser.open(file_name)
else:
    print("Failed to Download")