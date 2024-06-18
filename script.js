document.addEventListener("DOMContentLoaded", function () {
  fetch("options.json")
    .then((response) => response.json())
    .then((data) => {
      let stockOptions = document.getElementById("stockOptions");
      let lineOptions = document.getElementById("lineOptions");
      let stationName = document.getElementById("stationName");
      let newStationID = document.getElementById("newStationID");
      let fieldOptions = document.getElementById("fieldOptions");

      data.forEach((item) => {
        let stockOption = document.createElement("option");
        stockOption.value = item["股別"];
        stockOption.textContent = item["股別"];
        stockOptions.appendChild(stockOption);

        let lineOption = document.createElement("option");
        lineOption.value = item["線別"];
        lineOption.textContent = item["線別"];
        lineOptions.appendChild(lineOption);

        let stationOption = document.createElement("option");
        stationOption.value = item["車站中文名稱"];
        stationOption.textContent = item["車站中文名稱"];
        stationName.appendChild(stationOption);

        let stationIDOption = document.createElement("option");
        stationIDOption.value = item["新車站編號"];
        stationIDOption.textContent = item["新車站編號"];
        newStationID.appendChild(stationIDOption);

        let fieldOption = document.createElement("option");
        fieldOption.value = item["場別"];
        fieldOption.textContent = item["場別"];
        fieldOptions.appendChild(fieldOption);
      });
    })
    .catch((error) => console.error("Error loading JSON data:", error));
});
