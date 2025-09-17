from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

posts = [

    {
        'id': 1,
        'title': 'Python',
        'content': 'Python Programming language is high level language for ai and ml.'
    },
    {
        'id': 2,
        'title': 'JavaScript',
        'content': 'JavaScript used for web development'
    },
    {
        'id': 3,
        'title': 'C Programming language',
        'content': 'JavaScript used for embedded systems'
    }
]


def home(request):
    '''
    html = ""
    for post in posts:
        html += f"""
            <div>
            <a href=f"/post/{post['id']}">
            <h1>{post['id']} - {post['title']}</h1></a>
            <p>{post['content']}</p>
            </div>
        """
        '''
    context = {'posts':posts}
    return render(request , 'index.html' , context)

def single_post(request , id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            context = {'post':post}
            valid_id = True
            break
    if valid_id:
        return render(request , 'post.html' , context)
    else:
        return HttpResponseNotFound("404 Not Found") 
    
def google(request , id):
    url = reverse("post" , args=[id])
    return HttpResponseRedirect(url)
