const getLinks = async (url = '', requestAsJSON = {}) => {
    let links = [];
    let plcontinue = true;
    let query, json = {}, requestAsURL;
	while (plcontinue) {
		requestAsURL = new URLSearchParams(requestAsJSON).toString()
		const response = await fetch(url + requestAsURL)
        json = await response.json();
        ({ continue: { plcontinue } = {plcontinue:false}, query: { pages } } = json);

		for (const pageID in pages) {
            const pageLinks = pages[pageID].links;
			for (const linkObject in pageLinks) {
				links.push(pageLinks[linkObject].title)
			}
		}
        requestAsJSON.plcontinue = plcontinue;
    }
    return links;
}
const url = 'https://en.wikipedia.org/w/api.php?'
const data = {
	action: 'query',
	format: 'json',
	prop: 'links',
	titles: 'Hello'
}

getLinks(url, data).then((links) => console.log(links))
