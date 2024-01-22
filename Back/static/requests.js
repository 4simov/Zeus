const baseUrl = "http://10.121.128.165:5000/";

function getId() {
  return baseUrl.substring(7,19);
}

function toggleCheck(idSonde) {
    if(document.getElementById("checkbox" + idSonde).checked === true){
      //document.getElementById("g" + idSonde).style.backgroundColor = "white";
    } else {
      //document.getElementById("g" + idSonde).style.backgroundColor = "grey";
    }
  }

function GetSondeActivation(id) {
    var a1 = document.getElementById("myCheckbox" + id);
    if(a1.checked === true) {
        //location.reload();
        fetch(baseUrl +'sonde/' + id, {
            method: 'GET'
        })
        .then((response) => response.json())
        .then((response) => console.log(JSON.stringify(response)));
  }
}
/*

  async function GetReleve(idSonde) {
    await fetch('http://127.0.0.1:5000/releve-by-sonde/' + idSonde, {
            method: 'GET'
        })
        .then(async (response) => {
            const r = JSON.stringify(await response.json());

            console.log(r);
            data = r;
            console.log(data);
            return r;
        });
  }*/

  async function GetListSondes() {
    const r = await fetch(baseUrl + 'sonde', {
      method: 'GET'
    })
    .then(async (response) => {
      return await response.json()
    })
    
    return r;
  }
