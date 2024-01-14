
data = []

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

        /*const xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/releve-by-sonde/119");
        xhr.send();
        xhr.responseType = "json";
        xhr.onload = () => {
            if (xhr.readyState == 4 && xhr.status == 201) {
                const data = xhr.response;
                console.log(data);
            } else {
                console.log(`Error: ${xhr.status}`);
            }
        };*/
        
    }
    /*var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            alert(xhr.response);
        }
    }
    xhr.open('get', 'https://google.com', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    xhr.send();*/
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


  async function GetReleve(idSonde) {
    console.log(data);
    await fetch('http://127.0.0.1:5000/releve-by-sonde/' + idSonde, {
            method: 'GET'
        })
        .then(async (response) => {
            const r = await response.json();
            console.log(r);
            data = r;
        })

    console.log(data);
  }