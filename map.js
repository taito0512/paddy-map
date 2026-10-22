// 地図を作って、茨城県あたりを表示する
const map = L.map("map").setView([35.97, 140.02], 13);

// 背景の地図画像（OpenStreetMap）を敷く
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

// 自分のデータを読み込んで、地図に点を追加する
fetch("data/sample_polygons.geojson")
  .then(response => response.json())
  .then(data => {
    L.geoJSON(data).addTo(map);
  });
