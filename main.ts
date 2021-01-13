
const getLinks = async (url: any, requestAsJSON: any) => {
    const links = [];
    let nextPage: boolean|string = true;
    let query, json, requestAsURL: string, pages;
	while (nextPage) {
		requestAsURL = new URLSearchParams(requestAsJSON).toString()
		const response = await fetch(url + requestAsURL)
		json = await response.json();
		({ continue: { plcontinue: nextPage } = {plcontinue: false}, query: {pages} } = json);
		for (const pageID in pages) {
            const pageLinks = pages[pageID].links;
			for (const linkObject in pageLinks) {
				links.push(pageLinks[linkObject].title)
			}
		}
        requestAsJSON.plcontinue = nextPage;
    }
    return links;
}
const apiURL = 'https://en.wikipedia.org/w/api.php?'
const data = {
	action: 'query',
	format: 'json',
	prop: 'links',
	titles: 'Hello'
}

getLinks(apiURL, data).then((links) => console.log(links))
