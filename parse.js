const fetch = require("node-fetch");

const getData = async (url = '', requestAsJSON = {}) => {
    requestAsURL = new URLSearchParams(requestAsJSON).toString()
    const response = await fetch(url + requestAsURL);
    const json = await response.json();
    const pages = json.query.pages
    let links = []
    for (const pageID in pages) {
        const page = pages[pageID]
        const pageLinks = page.links
        for (const linkObject in pageLinks) {
            links.push(pageLinks[linkObject].title)
        }
    }
    return links
}

const url = "https://en.wikipedia.org/w/api.php?"
const data = {
        action: "query",
        format: "json",
        prop: "links",
        titles:"Hello"
    };

getData(url, data).then(links => console.log(links))