window.customElements.define('uscd-card-space', class extends HTMLElement{
    constructor(){
        super()
        this.data = null;
        this.render()
    }
    async connectedCallback(){
        try{
            console.log("This custom element loaded!")
        }catch(e){
            this.renderError(e)
        }
    }
    disconnectCallback(){
        console.log("custom element removed from the page!")
    }
    render(){
        const cardContent =`
        <article class="card card--featured lib-spaces-explore">
        <div class="card__body card--featured__body white-bg spaces">
            <picture>
                <source alt="Audrey's Cafe" srcset=${this.getAttribute('image-avif-src')} type="image/avif">
                <source alt="Audrey's Cafe" srcset=${this.getAttribute('image-webp-src')} type="image/webp">
                <img alt="" loading="lazy" src=${this.getAttribute('image-jpg-src')}>
            </picture>
            <a class="card__link-target" href="geisel-library/audreys-cafe.html"><h3>Audrey's Cafe<h3>
            </a>
                <span>Geisel 2 East</span>
            <p>Need some brain fuel? Audrey's Café offers a variety of food and drink to power your study session, all nestled in a cozy area with cafe table and chairs.</p>
        </div>
        <div class="card__toolbar">
            <a class="tag magenta" href="https://library.ucsd.edu/visit/study-spaces/browse-library-spaces.html?building=Geisel">Geisel</a>
            <a class="tag orange" href="https://library.ucsd.edu/visit/study-spaces/browse-library-spaces.html?space-category=general-study">                                            General Study</a>
            <a class="tag turquoise" href="https://library.ucsd.edu/visit/study-spaces/browse-library-spaces.html?noise-level=talking-permitted">                                            Talking Permitted</a>
        </div>
    </article>`
        this.innerHTML = cardContent;
    }
    renderError(e){
        console.error(e.message)
    }
})





/*

<div class="grid three-by-one">
    <article class="card card--featured lib-spaces-explore">
        <div class="card__body card--featured__body white-bg spaces">
            <picture>
                <source alt="Audrey's Cafe" srcset="https://library.ucsd.edu/_files/library-spaces-images/audreys_cafe.avif" type="image/avif">
                <source alt="Audrey's Cafe" srcset="https://library.ucsd.edu/_files/library-spaces-images/audreys_cafe.webp" type="image/webp">
                <img alt="${title}" loading="lazy" src="../../_files/library-spaces-images/audreys_cafe.jpg">
            </picture>
            <a class="card__link-target" href="geisel-library/audreys-cafe.html"><h3>Audrey's Cafe<h3>
            </a>
                <span>Geisel 2 East</span>
            <p>Need some brain fuel? Audrey's Café offers a variety of food and drink to power your study session, all nestled in a cozy area with cafe table and chairs.</p>
        </div>
        <div class="card__toolbar">
            <a class="tag magenta" href="https://library.ucsd.edu/visit/study-spaces/browse-library-spaces.html?building=Geisel">Geisel</a>
            <a class="tag orange" href="https://library.ucsd.edu/visit/study-spaces/browse-library-spaces.html?space-category=general-study">                                            General Study</a>
            <a class="tag turquoise" href="https://library.ucsd.edu/visit/study-spaces/browse-library-spaces.html?noise-level=talking-permitted">                                            Talking Permitted</a>
        </div>
    </article>
</div>
*/
