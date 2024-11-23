
import os
import google.generativeai as genai
from django.shortcuts import render
from django.contrib import messages


def chat(request):
    if request.method == 'POST':
        chattext = request.POST.get('chatque')
        
        if not chattext:
            messages.error(request, "Please enter a question.")
            return render(request, 'index.html')
        
        genai.configure(api_key="AIzaSyC4h8jQMwwu5foBgutLkydxXQvdNW3UicM")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(chattext)
        print(response.text)
        chat_answer = response.text
        messages.info(request, chat_answer)
        return render(request, 'index.html')

    return render(request, 'index.html')
