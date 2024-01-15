
function Graph(idSonde) {
    
    document.write(`

        <canvas id="myChart" style="position: relative; height:40vh; width:80vw"></canvas>

    `);
    
    // Données initiales
    var initialData = {
        labels: [],
        datasets: [{
          label: 'Température (°C)',
          data: [],
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
          fill: false
        }, {
          label: 'Humidité (%)',
          data: [],
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
          fill: false
        }]
    };
  
    // Configuration du graphique
    var options = {
        scales: {
          y: {
            beginAtZero: true
          }
        }
    };
  
    // Créer le graphique avec les données initiales
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'line',
      data: initialData,
      options: options
    });

    // Fonction pour ajouter des données au graphique
    function addData(chart, label, data) {
      chart.data.labels.push(label);
      chart.data.datasets.forEach((dataset, index) => {
        dataset.data.push(data[index]);
      });
    }

    function removeData(chart) {
        chart.data.labels = [];
        chart.data.datasets.forEach((dataset) => {
            dataset.data = [];
        });
        chart.update();
    }

    // Fonction pour mettre à jour le graphique avec de nouvelles données (simulé ici)
    async function updateChart() {
        removeData(myChart);
        await GetReleve(118);
        
        //addData(myChart, timestamp, [nouvelleLecture.temperature, nouvelleLecture.humidite]);
    }
  
      // Simuler la mise à jour toutes les quelques secondes
    setInterval(updateChart, 3000); // Mettez à jour toutes les 3 secondes (3000 millisecondes)
  
    // Fonction utilitaire pour générer un entier aléatoire dans une plage donnée (simulé ici)
    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    async function GetReleve(idSonde) {
        await fetch('http://127.0.0.1:5000/releve-by-sonde/' + idSonde, {
                method: 'GET'
            })
            .then(async (response) => {
                const r = await response.json();
    
                console.log(r);
                temp = [];
                hum = [];
                for (let index = 0; index < r.length; index++) {
                    addData(myChart, r[index]["date"].substr(0, 19), [r[index]["temperature"], r[index]["humidite"]]);
                    console.log(r[index]);
                }

                myChart.update();
            }); 
      }
}

function SetSondeActivation(id) {
    fetch('http://127.0.0.1:5000/sonde/' + id, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                activation: a1.checked
            })
        }
    )
    .then((response) => response.json())
    .then((response) => console.log(JSON.stringify(response)));
  }



