#Wiki

Project created as an assignemt for the cs50 Web Programming with Python and JavaScript course. 

Wiki is a Wikipedia-like online encyclopedia, built using Django framework, Python, CSS and HTML.
Several functions were implemented:
- Entry Page: visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, it renders a page that displays the contents of that encyclopedia entry.
- Index Page:  user can click on any entry name to be taken directly to that entry page.
- Search: the user is able to type a query into the search box in the sidebar to search for an encyclopedia entry and get an entry page as a result or display an error if such entry does not yet exist.
- New Page: clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry. Users are able to click a button to save their new page.
- Edit Page: on each entry page, the user is able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
- Random Page: Clicking “Random Page” in the sidebar takes user to a random encyclopedia entry.
- Markdown to HTML Conversion: On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. 
