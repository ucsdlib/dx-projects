/**
 * @element ucsd-library-news
 * @description A reusable component that displays a series UC San Diego Library news items in a panel display
 * @attr {string} items-to-display - [Optional] Positive integer, defaults to "3"
 * @attr {boolean} open-new-window - [Optional] Defaults to "_self"
 * @example
 * <ucsd-library-news></ucsd-library-news>
 * <ucsd-library-news items-to-display="6" open-new-window="true"></ucsd-library-news>
 * @author DT (UC San Diego Library Web Services)
 */

window.customElements.define('ucsd-library-news', class extends HTMLElement {

	constructor() {
		super();
		this.data = null;
	}

	async connectedCallback() {
		try {
			this.data = await this.loadData();
			this.render();
		} catch (e) {
			this.renderError(e);
		}
	}

	async loadData() {
		// Determine API's limit value based on custom element input
		let paramLimit = String(this.getAttribute('items-to-display') ?? '').trim();
		paramLimit = (/^(?:[1-9]\d*)$/u.test(paramLimit)) ? paramLimit : '3';

		/*
			API Endpoint: "https://today.ucsd.edu/news-and-features-api"
			Parameters: category, limit, offset, featured=1 (returns only featured stories)
			Category number corresponds to UC San Diego Today topic categories; separate multiple categories with "|"
			  - The Library is category "85"
		*/
		const response = await fetch("https://today.ucsd.edu/news-and-features-api?category=85&limit=" + paramLimit);
		return response.json();
	}

	render() {
		// Determine hyperlink's target value based on custom element input
		let attrTarget = this.getAttribute('open-new-window') === 'true';
		attrTarget = (attrTarget) ? '_blank' : '_self';

		let filling = '';
		filling = this.data.map(item => {
			// Set the channel path for special channels or use the default
			const urlChan = item.channel_id === 24 ? '/area-story/' : item.channel_id === 21 ? '/photo-essays/' : item.channel_id === 12 ? '/slideshows/' : item.channel_id === 17 ? '/videos/' : '/story/';
			// Set the image path to load a smaller image file or use the default
			const urlImage = item.teaser_photo ? (item.teaser_photo.includes("teaser_uploads/") ? item.teaser_photo.replace("teaser_uploads/", "teaser_uploads/_ucsd-feed/") : item.teaser_photo) : 'https://today.ucsd.edu/img/news-placeholder.jpg';

			// Output news item
			return `
				<li>
					<a class="news-item" href="https://today.ucsd.edu${urlChan}${item.url_title}" target="${attrTarget}">
						<div aria-hidden="true" class="center-page-news-thumbnail">
							<img alt="${item.pp_alt.replace(/"/g, "&quot;")}" src="${urlImage}">
						</div>
						<div class="center-page-news-title">${item.title}</div>
					</a>
				</li>
			`;
		}).join('');

		let bao = `
			<div class="row">
				<div class="col-md-12 lpw-news center-page-feed" id="center-page-news-events">
					<ul>
					${filling}
					</ul>
				</div>
			</div>
		`;
		this.innerHTML = bao;
	}

	renderError(e) {
		console.error('😵:', e.message);
	}

});

/**
 * @element ucsd-library-news-featured
 * @description A reusable component that displays news items whose `teaser_photo` filenames contain keyword tags (E.g., "totally-awesome-photo_HOMEPAGE.jpg" or "green-car_PRESSRELEASE.jpg")
 * @attr {string} tag - [Required] This is the keyword contained within a new item's `teaser_photo` filename (E.g., "_HOMEPAGE", "_PRESSRELEASE")
 * @attr {boolean} open-new-window - [Optional] Defaults to "_self"
 * @example
 * <ucsd-library-news-featured tag="_HOMEPAGE"></ucsd-library-news-featured>
 * <ucsd-library-news-featured tag="_PRESSRELEASE" open-new-window="true"></ucsd-library-news-featured>
 * @author DT (UC San Diego Library Web Services)
 */

window.customElements.define('ucsd-library-news-featured', class extends HTMLElement {

	constructor() {
		super();
		this.data = null;
		this.counter = 0;
	}

	async connectedCallback() {
		try {
			this.data = await this.loadData();
			this.render();
		} catch (e) {
			this.renderError(e);
		}
	}

	async loadData() {
		/*
			API Endpoint: "https://today.ucsd.edu/news-and-features-api"
			Parameters: category, limit, offset, featured=1 (returns only featured stories)
			Category number corresponds to UC San Diego Today topic categories; separate multiple categories with "|"
			  - The Library is category "85"
		*/
		const response = await fetch("https://today.ucsd.edu/news-and-features-api?category=85&limit=1000");
		return response.json();
	}

	render() {

		const attrTag = String(this.getAttribute('tag') ?? '').trim();

		// Determine hyperlink's target value based on custom element input
		let attrTarget = this.getAttribute('open-new-window') === 'true';
		attrTarget = (attrTarget) ? '_blank' : '_self';

		let filling = '';
		filling = this.data.map(item => {
			// Set the channel path for special channels or use the default
			const urlChan = item.channel_id === 24 ? '/area-story/' : item.channel_id === 21 ? '/photo-essays/' : item.channel_id === 12 ? '/slideshows/' : item.channel_id === 17 ? '/videos/' : '/story/';
			// Set the image path to load a smaller image file or use the default
			const urlImage = item.teaser_photo ? (item.teaser_photo.includes("teaser_uploads/") ? item.teaser_photo.replace("teaser_uploads/", "teaser_uploads/_ucsd-feed/") : item.teaser_photo) : 'https://today.ucsd.edu/img/news-placeholder.jpg';

			if (item.teaser_photo.includes(attrTag) && this.counter < 3)
			{
				this.counter++;
				// Output news item
				return `
					<li>
						<a class="news-item" href="https://today.ucsd.edu${urlChan}${item.url_title}" target="${attrTarget}">
							<div aria-hidden="true" class="center-page-news-thumbnail">
								<img alt="${item.pp_alt.replace(/"/g, "&quot;")}" src="${urlImage}">
							</div>
							<div class="center-page-news-title">${item.title}</div>
						</a>
					</li>
				`;
			}
			else {
				return '';
			}
		}).join('');

		let bao = `
			<div class="row">
				<div class="col-md-12 lpw-news center-page-feed" id="center-page-news-events">
					<ul>
					${filling}
					</ul>
				</div>
			</div>
		`;
		this.innerHTML = bao;
	}

	renderError(e) {
		console.error('😵:', e.message);
	}

});

/**
 * @element ucsd-library-news-featured-custom
 * @description A reusable component that takes a list of Today `entry_id` values as input and displays them. Note: NK prefers the "ucsd-library-news-featured" solution, but I am using custom element until the embedded tags are added to the `teaser_photo` filenames.
 * @attr {string} ids-to-display - [Required] This is a comma seperated list of three Today `entry_id` values (E.g., "16418, 16222, 15620")
 * @attr {boolean} open-new-window - [Optional] Defaults to "_self"
 * @example
 * <ucsd-library-news-featured-custom ids-to-display="16418, 16222, 15620"></ucsd-library-news-featured-custom>
 * <ucsd-library-news-featured-custom ids-to-display="16418, 16222, 15620" open-new-window="true"></ucsd-library-news-featured-custom>
 * @author DT (UC San Diego Library Web Services)
 */

window.customElements.define('ucsd-library-news-featured-custom', class extends HTMLElement {

	constructor() {
		super();
		this.data = null;
		this.counter = 0;
	}

	async connectedCallback() {
		try {
			this.data = await this.loadData();
			this.render();
		} catch (e) {
			this.renderError(e);
		}
	}

	async loadData() {

		/*
			API Endpoint: "https://today.ucsd.edu/news-and-features-api"
			Parameters: category, limit, offset, featured=1 (returns only featured stories)
			Category number corresponds to UC San Diego Today topic categories; separate multiple categories with "|"
			  - The Library is category "85"
		*/
		const response = await fetch("https://today.ucsd.edu/news-and-features-api?category=85&limit=1000");
		return response.json();
	}

	render() {

		let paramList = String(this.getAttribute('ids-to-display') ?? '').trim();
		paramList = paramList.split(",").map(s => Number(s.trim()));

		// Determine hyperlink's target value based on custom element input
		let attrTarget = this.getAttribute('open-new-window') === 'true';
		attrTarget = (attrTarget) ? '_blank' : '_self';

		let filling = '';
		filling = this.data.map(item => {
			// Set the channel path for special channels or use the default
			const urlChan = item.channel_id === 24 ? '/area-story/' : item.channel_id === 21 ? '/photo-essays/' : item.channel_id === 12 ? '/slideshows/' : item.channel_id === 17 ? '/videos/' : '/story/';
			// Set the image path to load a smaller image file or use the default
			const urlImage = item.teaser_photo ? (item.teaser_photo.includes("teaser_uploads/") ? item.teaser_photo.replace("teaser_uploads/", "teaser_uploads/_ucsd-feed/") : item.teaser_photo) : 'https://today.ucsd.edu/img/news-placeholder.jpg';

			if (paramList.includes(item.entry_id))
			{
				// Output news item
				return `
					<li>
						<a class="news-item" href="https://today.ucsd.edu${urlChan}${item.url_title}" target="${attrTarget}">
							<div aria-hidden="true" class="center-page-news-thumbnail">
								<img alt="${item.pp_alt.replace(/"/g, "&quot;")}" src="${urlImage}">
							</div>
							<div class="center-page-news-title">${item.title}</div>
						</a>
					</li>
				`;
			}
			else {
				return '';
			}
		}).join('');

		let bao = `
			<div class="row">
				<div class="col-md-12 lpw-news center-page-feed" id="center-page-news-events">
					<ul>
					${filling}
					</ul>
				</div>
			</div>
		`;
		this.innerHTML = bao;
	}

	renderError(e) {
		console.error('😵:', e.message);
	}

});