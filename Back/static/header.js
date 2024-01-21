
function head() {
    document.getElementById("header").innerHTML = `
    <header>
        <div class ="title">
            <h1>ZEUS</h1>
        </div>
        <div class = "infos">
            <div>
                <div class = "i">
                    <span id="datetime">
                    </span>
                </div>
                <div class = "i test">
                    <span id="ip">"ip : "</span>                
                </div>
            </div>
        </div>
    </header>
    `;
}