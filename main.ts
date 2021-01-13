
const getLinks = async (
	apiURL: string = 'https://en.wikipedia.org/w/api.php?',
	requestAsJSON: any = {
		action: 'query',
		format: 'json',
		prop: 'links',
		titles: 'Hello'
	}) => {
	const links = [];
	let nextPage: boolean | string = true;
	let query, json, requestAsURL: string, pages;
	while (nextPage) {
		requestAsURL = new URLSearchParams(requestAsJSON).toString()
		const response = await fetch(apiURL + requestAsURL)
		json = await response.json();
		({ continue: { plcontinue: nextPage } = { plcontinue: false }, query: { pages } } = json);
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
getLinks().then((links) => console.log(links))
