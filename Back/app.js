javascriptCopy code
document.addEventListener("DOMContentLoaded", function () {
    // Supposons que votre API renvoie un tableau de températures
    const apiEndpoint = "https://votre-api-meteo.com/températures"; // Remplacez cela par l'URL de votre API
    fetch(apiEndpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Mise à jour dynamique des barres de l'histogramme
            updateHistogram(data.temperatures);
        })
        .catch(error => {
            console.error("Erreur lors de la récupération des données de température :", error);
        });
});

function updateHistogram(temperatures) {
    temperatures.forEach((temp, index) => {
        const barElement = document.getElementById(`bar${index + 1}`);
        barElement.style.height = `${temp}%`;
    });
}
