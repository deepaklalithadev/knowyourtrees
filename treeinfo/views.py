from django.shortcuts import render, redirect
from .forms import treeform

# Create your views here.
from .models import treeinfo


def home(request):
    list = treeinfo.objects.all()
    return render(request,'treeinfo/home.html',{'treelist':list})


def detail(request,tree_id):
    tree = treeinfo.objects.get(id=tree_id)
    return render(request,'treeinfo/detail.html',{'tree':tree})

def add(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        sciname = request.POST.get('sciname', )
        localname1 = request.POST.get('localname1', )
        localname2 = request.POST.get('localname2', )
        desc = request.POST.get('desc', )
        uses = request.POST.get('uses', )
        maxheight = request.POST.get('maxheight', )
        lifespan = request.POST.get('lifespan', )
        timbervalue = request.POST.get('timbervalue', )
        avgtreeweight = request.POST.get('avgtreeweight', )
        matureage = request.POST.get('matureage', )
        req_soil = request.POST.get('req_soil', )
        req_temp = request.POST.get('req_temp', )
        req_water = request.POST.get('req_water', )
        req_rain = request.POST.get('req_rain', )
        req_alt = request.POST.get('req_alt', )
        req_girth = request.POST.get('req_girth', )
        req_other = request.POST.get('req_other', )
        treedesc = request.POST.get('treedesc', )
        trunkdesc = request.POST.get('trunkdesc', )
        leavesdesc = request.POST.get('leavesdesc', )
        flowerdesc = request.POST.get('flowerdesc', )
        other1desc = request.POST.get('other1desc', )
        other2desc = request.POST.get('other2desc', )
        treepic = request.FILES['treepic']
        trunkpic = request.FILES['trunkpic']
        leavespic = request.FILES['leavespic']
        flowerpic = request.FILES['flowerpic']
        other1pic = request.FILES['other1pic']
        other2pic = request.FILES['other2pic']
        newtree = treeinfo(name=name,sciname=sciname,localname1=localname1,localname2=localname2,
                           desc=desc,uses=uses,maxheight=maxheight,lifespan=lifespan,
                           timbervalue=timbervalue,avgtreeweight=avgtreeweight,matureage=matureage,
                           req_soil=req_soil,req_temp=req_temp,req_water=req_water,req_rain=req_rain,
                           req_alt=req_alt,req_girth=req_girth,req_other=req_other,treedesc=treedesc,
                           trunkdesc=trunkdesc,leavesdesc=leavesdesc,flowerdesc=flowerdesc,
                           other1desc=other1desc,other2desc=other2desc,treepic=treepic,trunkpic=trunkpic,
                           leavespic=leavespic,flowerpic=flowerpic,other1pic=other1pic,other2pic=other2pic)
        newtree.save()
    return render(request,'treeinfo/add.html')


def update(request,tid):
    treeinform = treeinfo.objects.get(id=tid)
    form = treeform(request.POST or None, request.FILES,instance=treeinfo)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'treeinfo/update.html',{'form':form,'treeinfo':treeinform})
