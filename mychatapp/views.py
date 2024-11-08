from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def chat(request):
    if request.method == 'POST':
        chattext = request.POST.get('chatque')
        print(chattext)
    import os
    import google.generativeai as genai

    genai.configure(api_key='AIzaSyC4h8jQMwwu5foBgutLkydxXQvdNW3UicM')

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )
    response = chat_session.send_message(chattext)

    print(response.text)
    chatans = response.text
    messages.info(request, chatans)
    # dic = {'ans' : chatans}
    return render(request, 'chat.html')