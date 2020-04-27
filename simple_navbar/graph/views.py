from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
from pylab import *

def index(request) :
    #plt.plot(range(10))

    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plt.plot(t, s, linewidth=1.0)
 
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'graph/index.html', {'data':uri})