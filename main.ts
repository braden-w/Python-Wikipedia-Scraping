const startWeb = async (startPage: string, endPage: string) =>
	{
	let done = false;
	const queue: string[] = [startPage];
	const web: any = {};
	let currentNode: string | undefined;
	let links = [];
	while (done === false) {
		currentNode = queue.shift();
		links = await getLinks(currentNode);
		links.forEach(link => {
			queue.push(link);
			web[link] = currentNode;
			if (link === endPage) {
				done = true;
			}
		});
	}
	return web;
}

const getLinks = async (
	title: string | undefined,
	apiURL: string = 'https://en.wikipedia.org/w/api.php?',
	requestAsJSON: any = {
		action: 'query',
		format: 'json',
		prop: 'links',
		titles: title
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
// console.log(await getLinks("Hello"))
var t0 = performance.now()

console.log(await startWeb("Feyerabend", "Germany"))
var t1 = performance.now()
console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.")
