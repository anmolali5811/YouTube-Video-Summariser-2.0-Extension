const Summarybtn = document.getElementById("summarise");
Summarybtn.addEventListener("click", function() {
    Summarybtn.disabled = true;
    Summarybtn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("summary");
            p.innerHTML = text;
            const div = document.getElementById("output");
            div.style.display = "block";
            Summarybtn.disabled = false;
            Summarybtn.innerHTML = "Summarise";
        }
        xhr.send();
    });
});

const Copybtn = document.getElementById("copy");
Copybtn.addEventListener("click", function() {
    var text = document.getElementById("summary").innerHTML;

    navigator.clipboard.writeText(text)
    .then(() => {
      alert(`Copied summary to clipboard`);
    })
    .catch((error) => {
      console.error(`Could not copy summary: ${error}`);
    });
});