// JavaScript code remains unchanged
var findMeButton = document.getElementById("findMeButton");
var map = L.map("map");
var marker, circle, zoomed;

map.setView([28.26689, 83.96851], 13);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
}).addTo(map);

findMeButton.addEventListener("click", () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
  } else {
    alert("Geolocation is not supported by your browser");
  }
});

function success(position) {
  const lati = position.coords.latitude;
  const longi = position.coords.longitude;
  const accuracy = position.coords.accuracy;

  if (marker) {
    map.removeLayer(marker);
    map.removeLayer(circle);
  }

  marker = L.marker([lati, longi]).addTo(map);
  circle = L.circle([lati, longi], { radius: accuracy }).addTo(map);
  if (!zoomed) {
    zoomed = map.fitBounds(circle.getBounds());
  }

  map.setView([lati, longi]);
}

function error(err) {
  if (err.code === 1) {
    alert("Please allow geolocation access");
  } else {
    alert("Unable to retrieve info");
  }
}
