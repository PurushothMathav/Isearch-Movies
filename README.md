# Movie Title Search

A simple web application that allows users to search for movie titles from a text file containing a list of movie titles and their corresponding URLs.

## Features

- User-friendly design with a responsive layout.
- Search functionality to find movies by keyword.
- Displays clickable links to movie URLs.
- Error handling for missing or incorrect file data.

## How to Use

1. Clone or download the repository to your local machine.
2. Place the `Movie titles.txt` file in the same directory as the HTML file. This text file should follow the structure:

## URL: <Movie URL> Title: <Movie Title>

Each movie should occupy two lines (one for the URL, one for the title), with no empty lines between them.
1. Open the `index.html` file in any modern web browser.
2. Enter a keyword in the search bar and click the "Search" button.
3. Matching movie titles and their URLs will be displayed in the results section.

## Requirements

- A modern web browser (e.g., Chrome, Firefox, Edge).
- A properly formatted `Movie titles.txt` file.

## File Structure

```plaintext
├── index.html  (HTML file containing the application code)
├── Movie titles.txt  (Text file containing movie data: URLs and titles)

## Technologies Used

1.HTML
2.CSS (for styling)
3.JavaScript (for functionality)

Customization
1.You can customize the design by modifying the CSS in the <style> section of the HTML file.
2.The script fetches the Movie titles.txt file dynamically, so you can update the file content without modifying the script.

Troubleshooting
1.If the application cannot find the Movie titles.txt file, ensure it is located in the same directory as the index.html file.
2.Check the browser console for any error messages if the application doesn't work as expected.
3.Make sure to check Name defined in html same as file name in the directory without any change. If you run locally, then
// const response = await fetch("Movie Titles.txt"); is enough. else you have to use
//const response = await fetch("./Movie%20Titles.txt");
