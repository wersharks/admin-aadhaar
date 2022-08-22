// Import the functions you need from the SDKs you need
import { getAuth, setPersistence, signInWithEmailAndPassword, browserSessionPersistence, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.9.3/firebase-auth.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.3/firebase-app.js";
import{
    getFirestore , doc, getDoc, setDoc, collection, addDoc, updateDoc, deleteDoc, deleteField
}
from "https://www.gstatic.com/firebasejs/9.9.3/firebase-firestore.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.9.3/firebase-analytics.js";




let name = document.getElementById("name");
let phone = document.getElementById("phone");
let email = "kamal@gmail.com";
let age = document.getElementById("age");
let gender = document.getElementById("gender");
let picture = document.getElementById("wizard-picture");
let password = "12345";


let centerUid = document.getElementById("centerUid"); //
let latLon = document.getElementById("latLon"); //
let operatorID = "12345f"; //
let isOperatorActive = true;
let ratings = "0";
let reviews = "";

let save = document.getElementById("save");


var admin = require("firebase-admin");

var serviceAccount = require("serviceAccountKey.json");

const app = admin.initializeApp({
credential: admin.credential.cert(serviceAccount),
databaseURL: "https://sportyme-9927c-default-rtdb.asia-southeast1.firebasedatabase.app"
});




// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDz1FziuD5dRY-hFw66gtIjaV9_R2ZE9ec",
  authDomain: "sportyme-9927c.firebaseapp.com",
  databaseURL: "https://sportyme-9927c-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "sportyme-9927c",
  storageBucket: "sportyme-9927c.appspot.com",
  messagingSenderId: "800240519039",
  appId: "1:800240519039:web:32e31e30d518fd5e51bc4a",
  measurementId: "G-JD0H8F9117"
};

// Initialize Firebase
// const app = initializeApp(firebaseConfig);


const db = getFirestore();

const auth = getAuth();
createUserWithEmailAndPassword(auth, email, password)
.then((userCredential) => {
    // Signed in 
    const user = userCredential.user;
    // ...
})
.catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    // ..
});

async function AddDocument_CustomID(){
    var ref = doc(db,"operators", name.value);

    const docRef = await setDoc(
        ref, {
            operatorID: operatorID,
            centerUid: centerUid.value,
            latLong: latLon.value,
            name: name.value,
            picture: picture.value,
            age: age.value,
            gender: gender.value,
            phone: phone.value,
            email: email.value,
            ratings: ratings,
            reviews: reviews,
            isOperatorActive: isOperatorActive,
            timestamp : Date.now()
        }
    )
    .then(()=>{
        alert("Operator Added Successfully");
    })
    .catch(error =>{
        alert("Error: " + error);
    });
}

save.addEventListener("click", AddDocument_CustomID);