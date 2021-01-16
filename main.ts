const startWeb = async (startPage: string, endPage: string) =>
{
	const queue: string[] = [startPage]
	const web: Record<string, string> = {};
	while (true) {
		const currentNodes = queue.splice(0, 200);
		const currentPromises = currentNodes.map(title => getLinks(title));
		const fulfilledPromises = await Promise.all(currentPromises);
		fulfilledPromises.forEach(fulfilledPromise => {
			fulfilledPromise.links.forEach(link => {
				queue.push(link);
				web[link] = fulfilledPromise.title!;
				if (link === endPage) {
					return web;
				}
			});
		});
	}
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
	await new Promise(r => setTimeout(r, 2000));
	while (nextPage) {
		requestAsURL = new URLSearchParams(requestAsJSON).toString();
		const json = await (await fetch(apiURL + requestAsURL)).json();
		({ continue: { plcontinue: nextPage } = { plcontinue: false }, query: { pages } } = json);
		for (const pageID in pages) {
			const pageLinks = pages[pageID].links;
			for (const linkObject in pageLinks) {
				links.push(pageLinks[linkObject].title)
			}
		}
		requestAsJSON.plcontinue = nextPage;
	}
	return { title: title, links: links };
}
// console.log(await getLinks("Hello"))
var t0 = performance.now()

// getLinks("Feyerabend").then(links => console.log(links));
// console.log(await getLinks("Feyerabend"));

// const gets = ["Feyerabend", "Hello", "There", "My", "Friend", "Enemy"]
// const getsPromises = gets.map(title => getLinks(title))
// console.log(await Promise.all(getsPromises));


// console.log(await startWeb("Feyerabend", "Germany"));
console.log(await startWeb("Feyerabend", "Gerhard Feyerabend"));

// getLinks("Feyerabend").then(links => {
// 	links.forEach(link => {
// 		console.log(link)
// 	})
// });

var t1 = performance.now()
console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.")
