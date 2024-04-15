

function refreshTime() {
  const timeDisplay = document.getElementById("time");
  const dateDisplay = document.getElementById("date");
  const dateString = new Date().toDateString();
  const time = new Date().toLocaleTimeString();
  timeDisplay.textContent = time;
  dateDisplay.textContent = dateString;
}
  setInterval(refreshTime, 1000);
