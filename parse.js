const fetch = require('node-fetch')

const getLinks = async (url = '', requestAsJSON = {}) => {
	let links = []
	// while (plcontinue) {
	requestAsURL = new URLSearchParams(requestAsJSON).toString()
	const response = await fetch(url + requestAsURL)
	const json = await response.json()
	const { continue: { plcontinue }, query: { pages } } = json

	for (const pageID in pages) {
		const page = pages[pageID]
		const pageLinks = page.links
		for (const linkObject in pageLinks) {
			links.push(pageLinks[linkObject].title)
		}
	}
	requestAsJSON.plcontinue = plcontinue
	// }
	return links
}
const url = 'https://en.wikipedia.org/w/api.php?'
const data = {
	action: 'query',
	format: 'json',
	prop: 'links',
	titles: 'Hello'
}

getLinks(url, data).then((links) => console.log(links))
