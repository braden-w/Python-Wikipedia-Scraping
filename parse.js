const fetch = require("node-fetch");

const url = "https://en.wikipedia.org/w/api.php?" +
    new URLSearchParams({
        action: "query",
        format: "json",
        prop: "links",
        titles:"Albert Einstein"
    });
async function f() {
    try {
        const req = await fetch(url);
        const json = await req.json();
        console.log(json.parse.text["*"]);
    } catch(e) {
        console.error(e);
        
    }

}
f()
