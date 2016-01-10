function process(data) {
    document.write(data.RWS[0].RW[0].FIS[0].FI[0].SHP[0].value[0] + "<br/>")
    document.write(convertCoords2LatLng(data.RWS[0].RW[0].FIS[0].FI[0].SHP[0].value[0]) + "<br/>");
}

function convertCoords2LatLng(coords) {
    var coordsSplit1 = coords.split(" ");
    var coordsSplit2 = [];

    for (i in coordsSplit1) {
        var temp = coordsSplit1[i].split(",")
        coordsSplit2.push({lat: parseFloat(temp[0]), lng: parseFloat(temp[1])});
    }
    return coordsSplit2;
}
