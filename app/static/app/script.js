//// DATE SETUP ////

let dateValue = document.querySelector('#calendar').value;
let monthValue = new Date().toJSON().slice(0, 7);

//// LIST AND CHARTS VIEWS ////

document.addEventListener('DOMContentLoaded', () => {
    let listView = document.querySelector('#list-view');
    let chartView = document.querySelector('#chart-view');
    let donutView = document.querySelector('#donut-view');
    let mapView = document.querySelector('#map-view');

    //// LIST VIEW ////

    // Setup for list calendar
    let listDate = document.querySelector('#list-date');

    // Enables list calendar date picking
    document.querySelector('#list-date').addEventListener('change', () => {
        build_list();
    })
    
    // List Enabler
    document.querySelector('#listBtn').addEventListener('click', () => {
        listView.style.display = 'block';
        chartView.style.display = 'none';
        mapView.style.display = 'none';
        donutView.style.display = 'none';
        linechartActive = false;
        donutchartActive = false;
        barchartActive = false
        build_list()
    })

    // Enables a "Back to Top" button when list is scrolled
    let topBtn = document.querySelector('#top-button');
    listView.addEventListener('scroll', () => {scroll_track()});
    
    // Shows "Back to Top" button when scrolled down
    function scroll_track() {
        if (listView.scrollTop > 20) {
            topBtn.style.display = 'block';
        } else {
            topBtn.style.display = 'none';
        }
    }

    // Returns to top on button click
    topBtn.addEventListener('click', () => {back_to_top()});
    function back_to_top() {
        listView.scrollTop = 0;
    }

    //// LIST BUILDER ////
    
    // Collects data from DB and builds list
    function build_list() {
        listDate = document.querySelector('#list-date').value;
        const tableBody = document.querySelector('#table-body');
        // Clears table
        document.querySelector('#table-body').innerHTML = "";
        
        let recordsCount = 0;
        fetch(`/build_list/${listDate}`)
        .then(response => response.json())
        .then(fires => {
            // Create a row for each fire data
            fires.forEach(fire => {
                recordsCount ++;
                const tableRow = document.createElement('tr');
                tableRow.tex = "row";
                const tableTS = document.createElement('td');
                const tableLat = document.createElement('td');
                const tableLon = document.createElement('td');
                const tableCity = document.createElement('td');
                const tableState = document.createElement('td');
                let rowDate = new Date(fire.date)
                tableTS.innerHTML = rowDate.toLocaleString('default', {dateStyle: 'medium'});
                tableLat.innerHTML = fire.latitude;
                tableLon.innerHTML = fire.longitude;
                tableCity.innerHTML = fire.city;
                tableState.innerHTML = fire.state;
                tableBody.append(tableRow)
                tableRow.append(tableTS, tableLat, tableLon, tableCity, tableState)
            })
        })
        .then(() => {document.querySelector('#list-records').innerHTML = recordsCount;})
    }

    //// CHARTS VIEW ////

    // Setup for charts switch
    let linechartActive = false;
    let donutchartActive = false;
    let barchartActive = false;

    // Sets variables for charts calendars manipulations
    let chartStart = document.querySelector('#chart-start');
    let chartEnd = document.querySelector('#chart-end');
    let chartMonthStart = document.querySelector('#month-start');
    let chartMonthEnd = document.querySelector('#month-end');
    let donutMonth = document.querySelector('#donut-month');
    
    // Sets date calendars prefilled values
    chartStart.value = chartEnd.value = dateValue;
    listDate.value = dateValue;

    // Sets month calendar prefilled values
    chartMonthStart.value = monthValue;
    chartMonthEnd.value = chartMonthStart.value;
    donutMonth.value = monthValue;

    // Enables donut chart calendar month picking
    document.querySelector('#donut-month').addEventListener('change', () => {
        build_donut();
    })

    // Enables line and bar charts calendar month picking
    document.querySelector('#month-start').addEventListener('change', () => {
        build_chart();
    })
    document.querySelector('#month-end').addEventListener('change', () => {
        // Sets max value for start input as the same of current end input
        document.querySelector('#month-start').max =
        document.querySelector('#month-end').value;
        // If the end month input is before start one, changes the start to the same month of end
        if (document.querySelector('#month-start').value > document.querySelector('#month-end').value) {
            document.querySelector('#month-start').value = document.querySelector('#month-end').value;
        }
        build_chart();
    })
    

    // Enables chart calendar day picking
    document.querySelector('#chart-start').addEventListener('change', () => {
        build_chart();
    })
    // Charts view: Prevents user input of a previous date for end or a later date for start
    document.querySelector('#chart-end').addEventListener('change', () => {
        // Sets max value for start input as the same of current end input
        document.querySelector('#chart-start').max =
        document.querySelector('#chart-end').value;
        build_chart();
        // If the end date input is before start one, changes the start to the same date of end
        if (document.querySelector('#chart-start').value > document.querySelector('#chart-end').value) {
            document.querySelector('#chart-start').value = document.querySelector('#chart-end').value;
        }
        build_chart()
    })

    // Donut Chart Enabler
    document.querySelector('#donutchartBtn').addEventListener('click', () => {
        if (donutchartActive == true) {
            mapView.style.display = 'block';
            donutView.style.display = 'none';
            chartView.style.display = 'none';
            listView.style.display = 'none';
            donutchartActive = false;
        } else {
            donutView.style.display = 'block';
            chartView.style.display = 'none';
            listView.style.display = 'none';
            mapView.style.display = 'none';
            linechartActive = false;
            donutchartActive = true;
            barchartActive = false;
            build_donut()
        }
    })

    // Line Chart Enabler
    document.querySelector('#linechartBtn').addEventListener('click', () => {
        if (linechartActive == true) {
            mapView.style.display = 'block';
            chartView.style.display = 'none';
            donutView.style.display = 'none';
            listView.style.display = 'none';
            linechartActive = false;
        } else {
            chartView.style.display = 'block';
            donutView.style.display = 'none';
            listView.style.display = 'none';
            mapView.style.display = 'none';
            linechartActive = true;
            donutchartActive = false;
            barchartActive = false;
            build_chart()
        }
    })
        
    // Bar Chart Enabler
    document.querySelector('#barchartBtn').addEventListener('click', () => {
        if (barchartActive == true) {
            mapView.style.display = 'block';
            chartView.style.display = 'none';
            donutView.style.display = 'none';
            listView.style.display = 'none';
            barchartActive = false;
        } else {
            chartView.style.display = 'block';
            donutView.style.display = 'none';
            listView.style.display = 'none';
            mapView.style.display = 'none';
            linechartActive = false;
            donutchartActive = false;
            barchartActive = true;
            build_chart()
        }
    })

    // Bar and Line charts period selector
    let rangeChosen = "day";
    let dayRange = document.querySelector('#day-range');
    let monthRange = document.querySelector('#month-range');
    // Switches chart view to months
    document.querySelector('#month-range').addEventListener('click', () => {
        chartStart.style.display = 'none';
        chartEnd.style.display = 'none';
        chartMonthStart.style.display = 'block';
        chartMonthEnd.style.display = 'block';
        dayRange.className = "dropdown-item";
        monthRange.className = "dropdown-item disabled";
        rangeChosen = "month";
    })
    // Switches chart view to days
    document.querySelector('#day-range').addEventListener('click', () => {
        chartStart.style.display = 'block';
        chartEnd.style.display = 'block';
        chartMonthStart.style.display = 'none';
        chartMonthEnd.style.display = 'none';
        dayRange.className = "dropdown-item disabled";
        monthRange.className = "dropdown-item";
        rangeChosen = "day";
    })
    

    //// CHART BUILDERS ////

    // Donut chart
    function build_donut() {
        let recordsNum = 0;
        let chartLabels = [];
        let chartData = [];
        donutMonth = document.querySelector('#donut-month').value;
        let date = new Date(donutMonth)
        let options = {
            month: 'short',
            day: 'numeric',
        }
        let options2 = {
            year: 'numeric',
            month:'short'
        }
        
        fetch(`/build_donut/${donutMonth}`)
        .then(response => response.json())
        .then(infos => {
            infos.forEach(info => {
                let donutLabelDate = new Date(info.date)
                chartLabels.push(donutLabelDate.toLocaleString('default', options))
            })
            infos.forEach(info => chartData.push(info.total));
            infos.forEach(info => {recordsNum = recordsNum + info.total})
        })
        .then(() => {
            // Plots donut chart
            if (donutchartActive == true) {
                let data = [{
                    values: chartData,
                    labels: chartLabels,
                    type: 'pie',
                    hole: .45,
                }];
                let layout = {
                    title: `${date.toLocaleDateString("en", options2)}` + "'s daily fire %",
                    annotations: [{
                        font: {
                            size: 11
                        },
                        showarrow: false,
                        text: "Records: " + recordsNum
                    }]
                };
                let config = {responsive: true}
                Plotly.newPlot('donut', data, layout, config)
            }
        })
    }

    // Line and bar charts
    function build_chart() {
        let chartLabels = [];
        let chartData = [];
        let startDate;
        let endDate;
        if (rangeChosen == "day") {
            startDate = document.querySelector('#chart-start').value;
            endDate = document.querySelector('#chart-end').value;
        } else if (rangeChosen == "month") {
            startDate = document.querySelector('#month-start').value;
            endDate = document.querySelector('#month-end').value;
        }
        fetch(`/build_chart/${rangeChosen}` + `/${startDate}` + `/${endDate}`)
        .then(response => response.json())
        .then(infos => {
            // Extracts data for the chart
            if (rangeChosen == "day") {
                infos.forEach(info => chartLabels.push(info.date));
                infos.forEach(info => chartData.push(info.total));
            } else if (rangeChosen == "month") {
                infos.forEach(info => chartLabels.push(info.month));
                infos.forEach(info => chartData.push(info.total));
            }
        })
        .then(() => {
            // Plots line chart
            if (linechartActive == true) {
                let data = [{
                    y: chartData,
                    x: chartLabels,
                    mode: 'lines',
                    line: {
                        color: 'rgb(255, 80, 0)',
                    },
                    type: 'scatter'
                }];
                let layout = {
                    xaxis: {title: "Day",},
                    yaxis: {title: "Fire count"},
                    title: "Fires per " + `${rangeChosen}`
                }
                let config = {responsive: true}
                Plotly.newPlot('chart', data, layout, config);
            // Plots Bar chart
            } else if (barchartActive == true) {
                let data = [{
                    x: chartLabels,
                    y: chartData,
                    type: 'bar',
                    marker: {color: 'rgb(255, 139, 51)'}
                }];
                let layout = {
                    title: "Fires per " + `${rangeChosen}`
                }
                let config = {responsive: true}
                Plotly.newPlot('chart', data, layout, config)
            }
        });

    }
});

//// MAP FUNCTIONS ////

// Sets firecounter
let firecounter = 0;

// Enables calendar date picking
document.querySelector('#calendar').addEventListener('change', () => {
    dateValue = String(document.querySelector('#calendar').value);
    firecounter = 0;
    activate_spinner();
    initMap();
})

// Sets cluster view toogle status
let clustersEnabled = true;

let map;
// Initializes and add the map
function initMap() {
    // Change single markers icon
    const icon = {
        url: "static/app/marker.svg",
        scaledSize: new google.maps.Size(5,5),
    }

    // Centers map
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 3.8,
        center: { lat: -13.625022, lng: -50.758556},
        mapTypeId: 'hybrid',
        disableDefaultUI: 'true',
    });
    
    let markers = [];
    // Collects fires data from DB
    fetch(`/get_fires/${dateValue}`)
    .then(response => response.json())
    .then(fires => {
            // Prevents error in case of empty values
            if (JSON.stringify(fires) !== '{}') {
                // Create a marker for each fire outbreak
                fires.forEach(fire => markers.push(create_marker(fire, map, icon)))
                    
                // Updates map fire counter stats
                document.querySelector('#firecount').innerHTML = `<strong>Fires: </strong>${firecounter}`;
            } else {
                document.querySelector('#firecount').innerHTML = "<strong>Fires: </strong> N/A";
            }
        }
    )
    .then(()=> {
        // Initiates marker clusterer or markers, whatever is enabled
        if (clustersEnabled == true) {
            new markerClusterer.MarkerClusterer({ map, markers });
        } else {
            clustersEnabled = false;
        }
    })

    // Gets % difference from previous day
    fetch(`get_difference/${dateValue}`)
    .then(response => response.json())
    .then(response => {
        // Outputs value to template
        if (response.Dif == "") {
            document.querySelector('#difPercent').innerHTML = "No data";
            document.querySelector('#difPercentCompl').innerHTML = " to compare"
        } else {
            document.querySelector('#difPercent').innerHTML = response.Dif + "%";
            document.querySelector('#difPercentCompl').innerHTML = " from last day"
        }
        // Changes text to red for fire increase, green for decrease and gray for all else
        if (response.Dif.startsWith("+") == true) {
            document.querySelector('#difPercent').className = "text-danger"
        } else if ((response.Dif.startsWith("-") == true)) {
            document.querySelector('#difPercent').className = "text-success"
        } else {
            document.querySelector('#difPercent').className = "text-secondary"
        }
    })
    .then(() => {
        clusterToggle.style.display = 'block'
        document.querySelector('#spinner').style.display = 'none'
    })
}
window.initMap = initMap;

// Enables creation of markers on the map
function create_marker(fire, map, icon) {
    
    // Sets the marker's location
    const location = { lat: parseFloat(fire.latitude), lng: parseFloat(fire.longitude) };

    // Sets marker
    const marker = new google.maps.Marker({
        position: location,
        icon: icon,
        map: map,
    });

    // Updates counter
    firecounter ++;

    return marker;
    // marker.setMap(map);
}

// Enables spinner and disables Cluster/Marker button while map loads them
// Prevents glitching the input
function activate_spinner() {
    clusterToggle.style.display = 'none';
    document.querySelector('#spinner').style.display = 'block';
}

// Toogles between Clusters and Markers views
let clusterToggle = document.querySelector('#clusterToggle');
document.addEventListener('DOMContentLoaded', function () {
    clusterToggle.addEventListener('click', () => {
        activate_spinner();
        dateValue = String(document.querySelector('#calendar').value)
        if (clustersEnabled == true) {
            clustersEnabled = false;
            clusterToggle.innerHTML = "Markers";
            clusterToggle.className = "btn btn-sm btn-outline-dark py-0 pointer-enabled"
        } else {
            clustersEnabled = true;
            clusterToggle.innerHTML = "Clusters";
            clusterToggle.className = "btn btn-sm btn-outline-dark py-0 pointer-enabled"
        }
        // Updates firecounter and reinitiates map
        firecounter = 0;
        initMap()
    })
})