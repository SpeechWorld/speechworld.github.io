document.addEventListener('DOMContentLoaded', () => {
    const subpageLinksContainer = document.getElementById('articles');

    fetch('metadata.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(publications => {
        publications.forEach(publication => {
            const article = document.createElement('article');
            article.itemScope = true;
            article.itemType = 'http://schema.org/Blog';
            
            const headline = document.createElement('h2');
            headline.className = "entry-title";
            headline.itemprop = 'headline';

            const link = document.createElement('a');
            link.href = `/${publication.id}`;
            link.textContent = publication.title;

            const span = document.createElement('span');
            span.className = 'entry-meta';
            
            const author = document.createElement('span');
            if (publication.authors) {
                author.itemprop = 'authors';
                author.textContent = `${publication.authors}`;
                span.appendChild(author);
            }

            const time = document.createElement('time');
            if (publication.datePublished) {
                const date = new Date(publication.datePublished);
                time.itemprop = 'datePublished';
                time.dateTime = date.toLocaleDateString('en-US', {year: 'numeric', month: '2-digit', day: '2-digit'});
                time.textContent = date.toLocaleDateString('en-US', {year: 'numeric', month: 'long', day: 'numeric'});
                span.appendChild(time);
            }


            headline.appendChild(link);
            article.appendChild(headline);
            article.appendChild(span);
            subpageLinksContainer.appendChild(article);
        })
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var navbarLinks = document.querySelectorAll("#navbar a");
    navbarLinks.forEach(function(link) {
        if (link.href === window.location.href) {
            link.classList.add("active");
        }
    });
});