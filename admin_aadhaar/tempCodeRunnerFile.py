for i in range(0,12):
        print("Time Slot: " + slots[i])
        bookings = db.collection(u'bookings').where(u'slotTime', u'==', slots[i]).stream()
        count=0
        for booking in bookings:
            count+=1
        print("Bookings: " + str(count))