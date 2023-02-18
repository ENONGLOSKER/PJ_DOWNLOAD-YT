from django.shortcuts import render
from pytube import YouTube
import  os

def downloader(request):
    global url

    url = request.GET.get('urls')
    yt = YouTube(url)
    video = []
    video = yt.streams.filter(progressive=True).all()
    print(video)
    embed_link = url.replace("watch?v=", "embed/")
    Title = yt.title

    context = {
        'video':video,
        'embed':embed_link,
        'title':Title,
    }
    return render(request, 'downloader.html',context)

def done(request, resolution):
    homedir = os.path.expanduser("~")
    dirs= homedir + '/Downloads'

    if request.method == 'POST':
        done = YouTube(url).streams.get_by_resolution(resolution)
        selesai = done.download(dirs)
        return render(request, 'dowld_done.html')
    else:
        return render(request, 'dowld_error.html')

    context = {
        'judul':'home',
    }
    return render(request, 'dowld_done.html',context)