let xValues = [];
let yValues = [];
let colors = ["blue", "red", "green", "orange", "purple"];
let backgroundColor = [];

for (let i = 0; i < content.length; i++) {
   xValues.push(content[i]["date"]);
   yValues.push(content[i]["hpm"]);

   backgroundColor.push(colors[i % colors.length]);
}

Chart.defaults.global.defaultFontColor = "white";

new Chart("sight-chart", {
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
         text: "Sight Reading Speed",
      },
      scales: {
         yAxes: [
            {
               // Configure y-axis options
               ticks: {
                  // Customize y-axis tick labels (optional)
               },
               scaleLabel: {
                  // Add y-axis label
                  display: true,
                  labelString: "Hits per Minute", // Your desired label text
               },
            },
         ],
         xAxes: [
            {
               // Configure y-axis options
               ticks: {
                  // Customize y-axis tick labels (optional)
               },
               scaleLabel: {
                  // Add y-axis label
                  display: true,
                  labelString: "Dates", // Your desired label text
               },
            },
         ],
      },
   },
});
