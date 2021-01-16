const startWeb = (startPage: string, endPage: string) =>
	{
	const queue: string[] = [startPage];
	const promiseQueue = [];
	const web: Record<string, string> = {};
	const processFirstQueue = () => {
		const currentNode: string | undefined = queue.shift();
		promiseQueue.push(getLinks(currentNode));
	}
	const processCompletedPromise = () {
		return Promise.all(promiseQueue).then(links => {
			links.forEach(link => {
				queue.push(link);
				web[link] = currentNode!;
				if (link === endPage) {
					return web;
				}
			});
		});
	}
	while (true) {
		while (queue.length < 200) {
			promiseQueue
		}
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

// console.log(startWeb("Feyerabend", "Germany"));
getLinks("Feyerabend").then(links => console.log(links))
getLinks("Feyerabend").then(links => console.log(links))
getLinks("Feyerabend").then(links => console.log(links))
getLinks("Feyerabend").then(links => console.log(links))
getLinks("Feyerabend").then(links => console.log(links))
getLinks("Feyerabend").then(links => console.log(links))
getLinks("Feyerabend").then(links => console.log(links))

// getLinks("Feyerabend").then(links => {
// 	links.forEach(link => {
// 		console.log(link)
// 	})
// });

var t1 = performance.now()
console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.")
