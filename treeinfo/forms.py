from django import forms
from .models import treeinfo


class treeform(forms.ModelForm):
    class Meta:
        model = treeinfo
        fields = ['name','sciname','localname1','localname2',
                  'desc','uses','maxheight','lifespan',
                   'timbervalue','avgtreeweight','matureage',
                   'req_soil','req_temp','req_water','req_rain',
                   'req_alt','req_girth','req_other','treedesc',
                   'trunkdesc','leavesdesc','flowerdesc',
                   'other1desc','other2desc','treepic','trunkpic',
                   'leavespic','flowerpic','other1pic','other2pic']