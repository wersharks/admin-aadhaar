let submit = document.getElementById("save");

var marker_auto, marker_nearby;

submit.addEventListener("click", function (e) {
  alert("Operator added Successfully");
});

//mapclick
var map = L.map("map", { doubleClickZoom: false }).locate({
  setView: true,
  maxZoom: 16,
});
// map.on("click", function (e) {
//   lat = e.latlng.lat;
//   lon = e.latlng.lng;

//   if (marker_auto != undefined) {
//     map.removeLayer(marker_auto);
//   }

//   //Add a marker_auto to show where you clicked.
//   marker_auto = L.marker([lat, lon]).addTo(map);
// });

map.on("locationfound", function (e) {
  var location_auto_img = L.icon({
    iconUrl: "../static/img/location_auto_img.png",
    iconSize: [30, 30],
  });
  var marker_auto = new L.marker(e.latlng, { icon: location_auto_img }).addTo(
    map
  );
  marker_auto.setLatLng(e.latlng);
  marker_auto.addTo(map);

  nearby_centres = async () => {
    const response = await fetch(
      "http://13.233.101.59:8080/aadhar/nearby/?x=" +
        e.latlng.lat +
        "&y=" +
        e.latlng.lng +
        "&radius=20",
      {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        method: "GET",
      }
    );
    const myJson = await response.json();

    console.log(myJson.data);

    myJson.data.forEach((element) => {
      // var nearby_img = L.icon({
      //     iconUrl: "../static/img/nearby_img.png",
      //     iconSize: [30, 30],
      // });
      var marker_nearby = new L.marker(
        [element.lat, element.lon],
        { riseOnHover: true }
        // { icon: nearby_img }
      );
      var popup = L.popup().setContent(
        "UID:" + element.uid + "\n" + "Location:" + element.location
      );
      marker_nearby.bindPopup(popup);

      marker_nearby.on("mouseover", function (e) {
        this.openPopup();
        console.log("open");
      });
      marker_nearby.on("mouseout", function (e) {
        this.closePopup();
      });

      marker_nearby.setLatLng([element.lat, element.lon]);
      marker_nearby.addTo(map).on("click", function (e) {
        document.getElementById("latLon").value =
          e.latlng.lat + "-" + e.latlng.lng;
        document.getElementById("centerUID").value = element.uid;
      });
    });
  };
  nearby_centres();
});

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  id: "examples.map-i875mjb7",
  noWrap: true,
}).addTo(map);
