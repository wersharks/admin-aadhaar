from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import auth, firestore, db, storage
from .forms import OperatorForm



cred = credentials.Certificate("admin_aadhaar/ServiceKey.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'sportyme-9927c.appspot.com'}) # connecting to firebase
db = firestore.client()

@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            img_object = form.instance
            print(form.cleaned_data)
            print("form is valid and saved")
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

        data = {
            "operatorId": "123456",
            "centerLocation": latLon,
            "centerUid": centerUid,
            "name": name,
            "picture": picture,
            "age": age,
            "gender": gender,
            "phoneNo": phone,
            "email": email,
            "ratings": "0",
            "reviews": [],
            "isOperatorActive": True,
            "timestamp": firestore.SERVER_TIMESTAMP
        }

        # Add a new doc in collection 'cities' with ID 'LA'
        # db.collection(u'operators').document(user.uid).set(data)

        # fileName = "admin_aadhaar/myimage.png"
        # bucket = storage.bucket()
        # blob = bucket.blob(fileName)
        # blob.upload_from_filename(fileName)

        # # Opt : if you want to make public access from the URL
        # blob.make_public()

        # print("your file url", blob.public_url)
        form = OperatorForm()
        return render(request, 'index.html', {'form': form, 'img_obj': img_object})

    else:
        form = OperatorForm()
    return render(request, 'index.html', {'form': form})