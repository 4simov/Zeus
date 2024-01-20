class Sondes{
  id;
  chart;

  constructor(idSonde) {
    this.id = idSonde;
  }


}

class Graphique {
  listSondes;
  activate = true;
  idInterval = 0;

  constructor() {
    console.log("edfsfer");
    this.loadListSonde()
    console.log("edfsfer------------------------");
  }

  async loadListSonde() {
    this.listSondes = [];
    const sondes = await GetListSondes();

    for (let index = 0; index < sondes.length; index++) {
      const element = sondes[index];
      const s = new Sondes(element["id"]);
      this.draw(s, index + 1);
      this.listSondes.push(s);
    }
  }

  draw(sonde, index) {
    document.write(`
    <div class = "panel-sonde">
        <div class ="inline-flex">
            <div>
                Sonde ` + index + ` 
            </div>
            <label class="switch">
                <input type="checkbox" id="checkbox` + sonde.id + `" onchange="SetSondeActivation(` + sonde.id +`)">
                <span class="slider round"></span>
            </label>
            <div>
                <span id="#dr` + sonde.id + `"></span>
            </div>
        </div>
        <div class = "panel-graph">
              <canvas id="myChart` + sonde.id + `" style="position: relative; height:40vh; width:80vw"></canvas>
        </div>
    </div>
        

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
    var ctx = document.getElementById('myChart' + sonde.id).getContext('2d');
    sonde.chart = new Chart(ctx, {
      type: 'line',
      data: initialData,
      options: options
    });
  }

  addData(sonde, label, data) {
    sonde.chart.data.labels.push(label);
    sonde.chart.data.datasets.forEach((dataset, index) => {
      dataset.data.push(data[index]);
    });
    sonde.chart.update();
    console.log(sonde.chart.data);
  }

  putData(sonde, listLabel, listTemps, listHums) {
    
    console.log("PUT ", sonde.chart);
    this.removeData(sonde);
    for (let index = 0; index < listLabel.length; index++) {
      console.log("---------");
      this.addData(sonde, listLabel[index], [listTemps[index], listHums[index]]);
    }
    console.log(sonde.chart.data);
  }

  removeData(sonde) {
    sonde.chart.data.labels = [];
    sonde.chart.data.datasets.forEach((dataset) => {
      dataset.data = [];
    });
  }

  updateAll() {
    
    
    for (let index = 0; index < this.listSondes.length; index++) {
      //const sonde = this.listSondes[index];
      this.updateChart(this.listSondes[index]);
      console.log(this.listSondes[index].data);
    }
    console.log("ça updateAll ! ", this.listSondes);
  }

  // Fonction pour mettre à jour le graphique avec de nouvelles données (simulé ici)
  async updateChart(sonde) {
    console.log("ça marche ! ", sonde);
    const b = await this.getSonde(sonde.id);
      if(b) {
        await this.getReleve(sonde);
      }
      //addData(myChart, timestamp, [nouvelleLecture.temperature, nouvelleLecture.humidite]);
  }

  async getSonde(id) {
    const r = await fetch ('http://127.0.0.1:5000/sonde/' + id, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
    .then(async (response) => {
      const json = await response.json();
      console.log("est-ce activer ? " + json["activate"]);
      return json["activate"];
    })
    
    return r;
  }

  setSondeActivation(id) {
    fetch('http://127.0.0.1:5000/sonde/' + id, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                activation: document.getElementById('myCheckbox1').checked
            })
        }
    )
    .then((response) => response.json())
    .then((response) => console.log(JSON.stringify(response)));
  }

  async getReleve(sonde) {
    await fetch('http://127.0.0.1:5000/releve-by-sonde/' + sonde.id, {
            method: 'GET'
        })
        .then(async (response) => {
            const r = await response.json();
            const listLabel = []; 
            const listTemp= []; 
            const listHum = [];
            for (let index = 0; index < r.length; index++) {
                //this.addData(this.myChart, r[index]["date"].substr(0, 19), [r[index]["temperature"], r[index]["humidite"]]);
                listLabel.push(r[index]["date"].substr(0, 19));
                listTemp.push(r[index]["temperature"]);
                listHum.push(r[index]["humidite"]);
            }
            document.getElementById('#dr' + sonde.id).textContent = "dernier relevé : " +r[0]["temperature"];
            console.log(sonde.chart);
            this.putData(sonde, listLabel, listTemp, listHum);
            console.log(sonde.chart.data);
            sonde.chart.update();
        }); 
  }
}

async function launchSonde() {
  const g = new Graphique();
  console.log(g.listSondes);
  setInterval( async () => { g.updateAll(); }, 2000);
}

async function GetSonde(id) {
  const r = await fetch ('http://127.0.0.1:5000/sonde/' + id, {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
  })
  .then(async (response) => {
    json = await response.json()
    return json["activate"];
  })
  
  return r;
}

function SetSondeActivation(id) {
    fetch('http://127.0.0.1:5000/sonde/' + id, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                activation: document.getElementById("checkbox" + id).checked
            })
        }
    )
    .then((response) => response.json())
    .then((response) => console.log(JSON.stringify(response)));
  }

  function test() {
      launchSonde();
  }

  function loadScript(src) {
    const script = document.createElement("Script");
    script.src = src;
    document.head.prepend(script);
  }

  /*function Graph(idSonde) {
    document.write(`
        <canvas id="myChart" style="position: relative; height:40vh; width:80vw"></canvas>
        
    `);
    test();

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
    
    // Simuler la mise à jour toutes les quelques secondes
    setInterval(function() { updateChart(idSonde) }, 3000); // Mettez à jour toutes les 3 secondes (3000 millisecondes)

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
    async function updateChart(idS) {
      b = await GetSonde(idS);
        if(b) {
          removeData(myChart);
          await GetReleve(118);
        }
        //addData(myChart, timestamp, [nouvelleLecture.temperature, nouvelleLecture.humidite]);
    }
  
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
                for (let index = 0; index < r.length; index++) {
                    addData(myChart, r[index]["date"].substr(0, 19), [r[index]["temperature"], r[index]["humidite"]]);
                }
                document.querySelector('#lr1').textContent = "dernier relevé : " +r[0]["temperature"];
                myChart.update();
            }); 
      }
}
*/