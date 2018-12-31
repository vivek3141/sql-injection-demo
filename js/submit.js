function makeHttpObject() {
    try {
        return new XMLHttpRequest();
    } catch (error) {
    }
    try {
        return new ActiveXObject("Msxml2.XMLHTTP");
    } catch (error) {
    }
    try {
        return new ActiveXObject("Microsoft.XMLHTTP");
    } catch (error) {
    }

    throw new Error("Could not create HTTP request object.");
}
const button = document.getElementById("submit");
button.addEventListener("click", e => {
    const code = document.getElementById("code").value;
    const url = "http://0.0.0.0:5000/search?code=" + code;
    let request = makeHttpObject();
    console.log(url);
    request.open("GET", url, true);
    request.send(null);
    request.onreadystatechange = function () {
        if (request.readyState == 4)
            var text = request.responseText;
        document.getElementById("text").innerHTML = text;
    };
});