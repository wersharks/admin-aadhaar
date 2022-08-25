from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import auth, firestore, db



cred = credentials.Certificate("admin_aadhaar/ServiceKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@csrf_exempt
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST.get('age')
        phone = request.POST['phone']
        email = request.POST['email']
        pswd = request.POST['pswd']
        gender = request.POST.get('gender')
        centerUid = request.POST.get('centerUid')
        latLon = request.POST.get('latLon')
        picture = request.FILES.get('wizard-picture')
        print(name, age, phone, email, gender, centerUid, latLon, picture, pswd)

        # user = auth.create_user(
        #     email=email,
        #     email_verified=True,
        #     password=pswd,
        #     display_name=name,
        #     photo_url=picture,
        #     disabled=False)
        # print('Sucessfully created new user: {0}'.format(user.uid))

        #

        # Add a new doc in collection 'cities' with ID 'LA'
#        db.collection(u'operators').document(user.uid).set(data)

        return render(request, 'index.html')
    return render(request, 'index.html')