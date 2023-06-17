import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import React from "react";
import "leaflet/dist/leaflet.css";
import icon from "../Images/icon.png";
import L from "leaflet";

export default function Map({ coords, display_name }) {
  const { latitude, longitude } = coords;

  const customIcon = new L.Icon({//creating a custom icon to use in Marker
    iconUrl: icon,
    iconSize: [25, 35],
    iconAnchor: [5, 30]
  });

  function MapView() {
    let map = useMap();
    map.setView([latitude, longitude], map.getZoom());
     //Sets geographical center and zoom for the view of the map
    return null;
  }
  var locations = [
    ["LOCATION_1", 11.8166, 122.0942],
    ["LOCATION_2", 11.9804, 121.9189],
    ["LOCATION_3", 10.7202, 122.5621],
    ["LOCATION_4", 11.3889, 122.6277],
    ["LOCATION_5", 10.5929, 122.6325]
  ];

  return (
    <MapContainer
      classsName="map"
      center={[latitude, longitude]}
      zoom={10}
      scrollWheelZoom={true}
    >
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> 
        contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker icon={customIcon} position={[latitude, longitude]}>
        <Popup>"hello"</Popup>
      </Marker>
     
      <MapView />
    </MapContainer>
    
  );
}