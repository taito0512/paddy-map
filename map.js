function rowsToGeoJSON(rows) {
  return {
    type: "FeatureCollection",
    features: rows.map(row => ({
      type: "Feature",
      geometry: { type: "Point", coordinates: [row[2], row[1]] },
      properties: { final_label: row[3] }
    }))
  };
}


// 地図を作って、茨城県あたりを表示する
const map = L.map("map").setView([35.97, 140.02], 13);
// 背景の地図画像（OpenStreetMap）を敷く
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

let currentLayer = null;  // 今表示しているレイヤーを覚えておく箱

function loadParcels(threshold) {
  fetch(`http://127.0.0.1:8000/parcels?region=82350&threshold=${threshold}`)
    .then(response => response.json())
    .then(data => {
      if (currentLayer) {
        map.removeLayer(currentLayer);   // 前の色分けを消す
      }
      currentLayer = L.geoJSON(rowsToGeoJSON(data) , {
       pointToLayer: (feature, latlng) => {
          const color = feature.properties.final_label === "水田" ? "green" : "red";
          return L.circleMarker(latlng, { color: color, radius: 5 });
        }
      }).addTo(map);
    });
}

const slider = document.getElementById("threshold");
const label = document.getElementById("threshold-label");

slider.addEventListener("input", () => {
  label.textContent = slider.value;
  loadParcels(slider.value);
});

loadParcels(0);  // 最初の表示
