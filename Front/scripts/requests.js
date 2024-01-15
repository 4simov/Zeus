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
        fetch('http://127.0.0.1:5000/sonde/' + id, {
            method: 'GET'
        })
        .then((response) => response.json())
        .then((response) => console.log(JSON.stringify(response)));
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