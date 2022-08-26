from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import auth, firestore, db
from uploadimages.models import UploadImage
import base64





cred = credentials.Certificate("admin_aadhaar/ServiceKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@csrf_exempt
def home(request):
    if request.method == 'POST':
        # form = UploadImage(request.POST, request.FILES)  
        # if form.is_valid():  
        #     form.save()  
    
        #     # Getting the current instance object to display in the template  
        #     img_object = form.instance  
                
        #     return render(request, 'image_form.html', {'form': form, 'img_obj': img_object}) 
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
        # with open(picture, "rb") as image_file:
        #     encoded_string = base64.b64encode(image_file.read())
        # print(encoded_string)

        user = auth.create_user(
            email=email,
            email_verified=True,
            password=pswd,
            display_name=name,
            photo_url=picture,
            disabled=False)
        print('Sucessfully created new user: {0}'.format(user.uid))

        data = {
            "operatorId": user.uid,
            "centerLocation": latLon,
            "centerUid": centerUid,
            "name": name,
            "picture": picture,
            "age": age,
            "gender": gender,
            "phoneNo": "+91" + phone,
            "email": email,
            "ratings": "0",
            "reviews": [],
            "isOperatorActive": True,
            "timestamp": firestore.SERVER_TIMESTAMP
            
        }

        # Add a new doc in collection 'cities' with ID 'LA'
        db.collection(u'operators').document(user.uid).set(data)

        return render(request, 'index.html')
    #else:
        #form = UploadImage()
    return render(request, 'index.html')