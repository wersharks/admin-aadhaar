from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse
import firebase_admin
from firebase_admin import credentials
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import auth, firestore, db
from uploadimages.models import UploadImage
import base64
import json
from rest_framework.views import APIView, status
from rest_framework.response import Response





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

class my_dictionary(dict):
     
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function to add key:value
  def add(self, key, value):
    self[key] = value
 
 


class slotBookings(APIView):
    

    # operator = db.collection(u'Operators').where("centerUid", "==", centerUid).get()
    # print(operator)
    slots = [
        "9:00 AM - 9:30 AM",
        "9:30 AM - 10:00 AM",
        "10:00 AM - 10:30 AM",
        "10:30 AM - 11:00 AM",
        "11:00 AM - 11:30 AM",
        "11:30 AM - 12:00 PM",
        
        "2:00 PM - 2:30 PM",
        "2:30 PM - 3:00 PM",
        "3:00 PM - 3:30 PM",
        "3:30 PM - 4:00 PM",
        "4:00 PM - 4:30 PM",
        "4:30 PM - 5:00 PM"
    ]

    #operators = db.collection(u'operators').where(u'centerUid', u'==', cUid).stream()

    # for slot in slots:
    #     mslot[slot] = db.collection(u'bookings').where(u'slotTime', u'==', slots[slot]).stream()
    #     eslot[slot] = db.collection(u'bookings').where(u'slotTime', u'==', slots[slot+6]).stream()

        
    # mslot0 = db.collection(u'bookings').where(u'slotTime', u'==', slots[0]).stream()
    # mslot1 = db.collection(u'bookings').where(u'slotTime', u'==', slots[1]).stream()
    # mslot2 = db.collection(u'bookings').where(u'slotTime', u'==', slots[2]).stream()
    # mslot3 = db.collection(u'bookings').where(u'slotTime', u'==', slots[3]).stream()
    # mslot4 = db.collection(u'bookings').where(u'slotTime', u'==', slots[4]).stream()
    # mslot5 = db.collection(u'bookings').where(u'slotTime', u'==', slots[5]).stream()

    # eslot0 = db.collection(u'bookings').where(u'slotTime', u'==', slots[6]).stream()
    # eslot1 = db.collection(u'bookings').where(u'slotTime', u'==', slots[7]).stream()
    # eslot2 = db.collection(u'bookings').where(u'slotTime', u'==', slots[8]).stream()
    # eslot3 = db.collection(u'bookings').where(u'slotTime', u'==', slots[9]).stream()
    # eslot4 = db.collection(u'bookings').where(u'slotTime', u'==', slots[10]).stream()
    # eslot5 = db.collection(u'bookings').where(u'slotTime', u'==', slots[11]).stream()



    # dict_obj = my_dictionary()
    
    # for i in range(0,12):
    #     bookings = db.collection(u'bookings').where(u'slotTime', u'==', slots[i]).stream()
    #     count=0
    #     for booking in bookings:
    #         count+=1
        
    #     dict_obj.add(slots[i], count)
    # print(dict_obj)



    # oId = "9yJLSrpjZUQxkK2wnGSCDLSud6m1"
    # print("Time Slot   " + oId)
    # bookings = db.collection(u'bookings').where(u'operatorId', u'==', mslot0).stream()
    # for booking in bookings:
    #     print("BOOKING    " + f'{booking.id}')

        

    # doc_id = "7thR2wPfoG9BpVhgiu5B"
    # doc = db.collection("operators").document(doc_id).get()

    # # View document data
    # print("Document Id", doc.id) # Get document id
    # print("Get single field", doc.get("name")) # Get single value by key
    # print("Document to Dictionary", doc.to_dict()) # Get all document data  as dictionary



    # for update in updation:
    #     print(f'{update.id} => {update.to_dict()}')

    # newEnrollment = db.collection(u'operators').where(u'bookingType', u'==', 1).stream()

    # for newEnroll in newEnrollment:
    #     print(f'{newEnroll.id} => {newEnroll.to_dict()}')

    def get(self, request, format=None):
        slots = [
            "9:00 AM - 9:30 AM",
            "9:30 AM - 10:00 AM",
            "10:00 AM - 10:30 AM",
            "10:30 AM - 11:00 AM",
            "11:00 AM - 11:30 AM",
            "11:30 AM - 12:00 PM",
            
            "2:00 PM - 2:30 PM",
            "2:30 PM - 3:00 PM",
            "3:00 PM - 3:30 PM",
            "3:30 PM - 4:00 PM",
            "4:00 PM - 4:30 PM",
            "4:30 PM - 5:00 PM"
        ]
        dict_obj = my_dictionary()
        for i in range(0,12):
            bookings = db.collection(u'bookings').where(u'slotTime', u'==', slots[i]).stream()
            count=0
            for booking in bookings:
                count+=1
            dict_obj.add(slots[i], count)
        print(dict_obj)

        # oId = "9yJLSrpjZUQxkK2wnGSCDLSud6m1"
        # bookings = db.collection(u'bookings').where(u'operatorId', u'==', oId).stream()
        # for booking in bookings:
        #     bookingId = booking.id
        #     operatorId= booking.get("operatorId")
        #     bookingLocation = booking.get("bookingLocation")

            # value = {
            #     "slotCounts": slotCounts,
            #     "slotTime": slots
            # } 

            
        return Response(dict_obj)

    
class booktype(APIView):
    def get(self, request, format=None):
        enrollment = db.collection(u'bookings').where(u'bookingType', u'==', 1).stream()
        for enroll in enrollment:
            print(f'{enroll.id} => {enroll.to_dict()}')
        return Response(enroll)
