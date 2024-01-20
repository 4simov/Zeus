
baseUrl = "http://192.168.1.62:5000/";

class Sondes{
  id;
  chart;
  ctx;
  constructor(idSonde) {
    this.id = idSonde;
  }


}

class Graphique {
  listSondes;
  activate = true;
  idInterval = 0;

  constructor() {
    this.loadListSonde();
  }

  async loadListSonde() {
    this.listSondes = [];
    const sondes = await GetListSondes();

    for (let index = 0; index < 1; index++) {
      const element = sondes[index];
      const s = new Sondes(element["id"]);
      this.draw(s, s.id);
      this.initData(s);
      this.listSondes.push(s);
    }
  }

  draw(sonde, adress) {
    document.getElementById("b").innerHTML += `
      <div class = "panel-sonde">
          <div class ="inline-flex">
              <div>
                  Sonde ` + adress + ` 
              </div>
              <label class="switch">
                  <input type="checkbox" id="checkbox` + sonde.id + `" onchange="SetSondeActivation(` + sonde.id +`)">
                  <span class="slider round"></span>
              </label>
              <div>
                  <span id="#dr` + sonde.id + `"></span>
              </div>
          </div>
          <div>
                <canvas id="myChart` + sonde.id + `" style="position: relative; height:40vh; width:80vw"></canvas>
          </div>
      </div>
    
    `;
  }

  initData(sonde) {
    // Données initiales
    const initialData = {
        labels: [],
        datasets: [{
          label: 'Température (°C)',
          data: [],
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          pointBackgroundColor : function(context) {
            var index = context.dataIndex;
            var value = context.dataset.data[index];
            return value < 16 ? 'blue' :    // else, alternate values in blue and green
                    'green';
          },
          pointRadius : 15,
          pointHoverRadius : 30,
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
          fill: false
        },
        {
          label: 'Humidité (%)',
          data: [],
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
          fill: false
        }]
    };
  
    // Configuration du graphique
    const options = {
        scales: {
          y: {
            beginAtZero: true
          }
        },
        animation: {
          duration: 0
      }
    };
  
    // Créer le graphique avec les données initiales
    sonde.ctx = document.getElementById('myChart' + sonde.id).getContext('2d');
    //Déclare le render du graphe
    sonde.chart = new Chart(sonde.ctx, {
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
  }

  putData(sonde, listLabel, listTemps, listHums) {
    this.removeData(sonde);
    for (let index = 0; index < listLabel.length; index++) {
      this.addData(sonde, listLabel[index], [listTemps[index], listHums[index]]);
    }
  }

  removeData(sonde) {
    sonde.chart.data.labels = [];
    sonde.chart.data.datasets.forEach((dataset) => {
      dataset.data = [];
    });
  }

  updateAll() {
    for (let index = 0; index < this.listSondes.length; index++) {
      this.updateChart(this.listSondes[index]);
    }
    Window.onload = function() {
      for (let index = 0; index < this.listSondes.length; index++) {
        console.log(this.listSondes[index].chart.data);
        //window.myLine = this.listSondes[index].chart;
      }
    }


  }

  // Fonction pour mettre à jour le graphique avec de nouvelles données (simulé ici)
  async updateChart(sonde) {
    const b = await this.getSonde(sonde.id);
    document.getElementById("checkbox"+sonde.id).checked = b;
      if(b) {
        await this.getReleve(sonde);
      }
      //addData(myChart, timestamp, [nouvelleLecture.temperature, nouvelleLecture.humidite]);
  }

  async getSonde(id) {
    const r = await fetch (baseUrl+'sonde/' + id, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    })
    .then(async (response) => {
      const json = await response.json();
      return json["activate"];
    })
    
    return r;
  }

  setSondeActivation(id) {
    fetch(baseUrl+'sonde/' + id, {
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
    await fetch(baseUrl+'releve-by-sonde/' + sonde.id, {
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
            this.putData(sonde, listLabel, listTemp, listHum);
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
  const r = await fetch (baseUrl+'sonde/' + id, {
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
    fetch(baseUrl+'sonde/' + id, {
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
