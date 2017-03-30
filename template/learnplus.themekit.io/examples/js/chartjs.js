(function ($) {

    function hexToRgb(hex) {
      var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
      return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
      } : null;
    }

    function rgbPerc(hex, percentage) {
      return 'rgba('+
        hexToRgb(hex).r + ',' + 
        hexToRgb(hex).g + ',' + 
        hexToRgb(hex).b + ', '+ 
        percentage +')';
    }

    // LINE
    var linedata = {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      color: colors['chart-primary'],
      datasets: [{
        label: "Label",
        fill: true,
        backgroundColor: rgbPerc( colors[ 'chart-primary' ], .1),
        borderColor: colors[ 'chart-primary' ],
        borderCapStyle: 'butt',
        borderJoinStyle: 'miter',
        pointBorderWidth: 5,
        pointBorderColor: colors[ 'chart-primary' ],
        pointBackgroundColor: colors[ 'chart-primary' ],
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderWidth: 0, 
        data: [10, 59, 23, 81, 56, 55, 40]
      }]
    };

    if ($("#lineChart").length) {
      new Chart($("#lineChart"), {
        type: 'line',
        data: linedata,
        options: {
          legend: {
            display: false
          },
          scales: {
            xAxes: [{
              display: false
            }],
            yAxes: [{
                ticks: {
                  fontColor: rgbPerc(colors[ 'chart-primary' ],.84),
                  fontStyle: '500',
                  fontSize: 14,
                  beginAtZero: true
                },
                gridLines: {
                  color:  rgbPerc(colors[ 'chart-primary' ], .1),
                  zeroLineColor:  rgbPerc(colors[ 'chart-primary' ], .2)
                }
            }]
          }
        },
      });
    }

    // BAR
    var bardata = {
        labels: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K"],
        datasets: [
            {
                label: "",
                backgroundColor: "#ffffff",
                borderColor: colors[ 'chart-primary' ],
                hoverBackgroundColor: rgbPerc("#ffffff", .4),
                data: [65, 59, 80, 81, 56, 55, 40, 81, 56, 55, 40],
            }
        ]
    };
    if ($("#barChart").length) {
      new Chart($("#barChart"), {
        type: 'bar',
        data: bardata,
        options: {
          legend: {
            display: false
          },
          scales: {
            xAxes: [{
              display: false
            }],
            yAxes: [{
              ticks: {
                beginAtZero:true,
                fontColor: "#ffffff"
              },
              gridLines: {
                color: "rgba(255,255,255, 0.2)",
                zeroLineColor:  "rgba(255, 255, 255, 0.2)"
              }
            }],
          },
          tooltips: {
            backgroundColor: '#212121',
            cornerRadius: 3,
            caretSize: 0
          },
        },
      });
    }
    
    // RADAR
    var radardata = {
      labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"],
      datasets: [{
        label: "My First dataset",
        backgroundColor: rgbPerc(colors['primary-color'], .2),
        borderColor: colors[ 'chart-primary' ],
        pointBackgroundColor:  colors[ 'chart-primary' ],
        pointBorderColor: "#fff",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgba(179,181,198,1)",
        data: [65, 59, 90, 81, 56, 55, 40]
      }]
    };

    if ($("#radarChart").length) {
      new Chart($("#radarChart"), {
        type: 'radar',
        data: radardata
      });
    }

    // POLAR
    var polardata = {
      datasets: [{
        data: [11,16,7,14,3,],
        backgroundColor: [
          colors['chart-primary'],
          colors['chart-secondary'],
          colors['chart-third'],
          colors['purple-500'],
          colors['grey-500'],
        ],
        label: 'Dataset' // for legend
      }],
      labels: [
        "Color #1",
        "Color #2",
        "Color #3",
        "Color #4",
        "Color #5",
      ]
    };

    if ($("#polarChart").length) {
      new Chart($("#polarChart"), {
        data: polardata,
        type: 'polarArea',
        options: {
          elements: {
            arc: {
              borderColor: "#ffffff"
            }
          }
        }
      });
    }

    var piedata = {
      labels: [
        "Color 1",
        "Color 2",
        "Color 3"
      ],
      datasets: [{
        data: [300, 50, 100],
        backgroundColor: [
          colors['chart-primary'],
          colors['chart-secondary'],
          colors['chart-third']
        ],
        hoverBackgroundColor: [
          rgbPerc(colors['chart-primary'], .84),
          rgbPerc(colors['chart-secondary'], .84),
          rgbPerc(colors['chart-third'], .84)
        ]
      }]
    };

    // PIE
    if ($("#pieChart").length) {
      new Chart($("#pieChart"), {
        type: 'pie',
        data: piedata
      });
    }

    var donutdata = {
      labels: [
        "Color 1",
        "Color 2",
        "Color 3"
      ],
      datasets: [{
        data: [300, 50, 100],
        backgroundColor: [
            colors['chart-primary'],
            colors['chart-secondary'],
            colors['chart-third']
        ],
        hoverBackgroundColor: [
            rgbPerc(colors['chart-primary'], .84),
            rgbPerc(colors['chart-secondary'], .84),
            rgbPerc(colors['chart-third'], .84)
        ]
      }]
    };

    // Donut
    if ($("#donutChart").length) {
      new Chart($("#donutChart"), {
        type: 'doughnut',
        data: donutdata
      });
    }

}(jQuery));