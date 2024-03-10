let colors = ["blue", "red", "green", "orange", "purple"];

Chart.defaults.global.defaultFontColor = "#D3D3D3";

function timeToSeconds(time) {
   let parts = time.split(":");
   parts = parts[0] * 1 + parts[1] / 60;
   return parts.toFixed(2);
}

for (let key in content) {
   let xValues = [];
   let yValues = [];
   let backgroundColor = [];

   for (let value in content[key]) {
      xValues.push(content[key][value]["date"]);
      yValues.push(timeToSeconds(content[key][value]["time"]));

      backgroundColor.push(colors[value % colors.length]);
   }
   new Chart(key + "-chart", {
      type: "line",
      data: {
         labels: xValues,
         datasets: [
            {
               backgroundColor: backgroundColor,
               data: yValues,
            },
         ],
      },
      options: {
         legend: { display: false },
         title: {
            display: true,
            text: "Scales and Chords Speed",
         },
         scales: {
            yAxes: [
               {
                  scaleLabel: {
                     display: true,
                     labelString: "Time (lower is better)",
                  },
               },
            ],
            xAxes: [
               {
                  scaleLabel: {
                     display: true,
                     labelString: "Dates",
                  },
               },
            ],
         },
      },
   });
}
