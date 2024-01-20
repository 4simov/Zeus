baseUrl = "http://192.168.1.62:5000/";

function toggleCheck() {
    if(document.getElementById("myCheckbox").checked === true){
      document.getElementById("aLink").style.display = "block";
    } else {
      document.getElementById("aLink").style.display = "none";
    }
  }

function GetSondeActivation(id) {
    var a1 = document.getElementById("myCheckbox1");
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
