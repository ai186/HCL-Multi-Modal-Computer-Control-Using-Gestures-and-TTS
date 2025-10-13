document.getElementById("startGesture").addEventListener("click", () => {
    fetch("/start-gesture", { method: "POST" })
        .then(response => response.json())
        .then(data => alert("Gesture Control Started: " + data.message))
        .catch(error => console.error("Error:", error));
});

document.getElementById("stopGesture").addEventListener("click", () => {
    fetch("/stop-gesture", { method: "POST" })
        .then(response => response.json())
        .then(data => alert("Gesture Control Stopped: " + data.message))
        .catch(error => console.error("Error:", error));
});
