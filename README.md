# Future Factory Website

The website for the https://futurefactory.nl.

Extensive documentation can be found at https://roboteamtwente.github.io/future_factory_website

This website is build with Django as a back-end server and uses a template from 
[Creative Studio](https://www.free-css.com/free-css-templates/page286/creative-studio), which makes use of NPM and 
gulpfile.js in order to generate all the files.

# Getting started
This project requires a working python installation and NPM.

1. Clone this repository
2. Install the requirements with `pip install -r requirements.txt`
3. Set environment variables
   - `DEBUG` should be `TRUE` during development.
     - This will create a local database.
   - `DJANGO_KEY` set this to a random string.
   - `BETA` is deprecated.
4. Run the migrations with `python manage.py migrate`
5. Create a superuser with `python manage.py createsuperuser`
6. Run `python manage.py runserver`

You should now be able to open the local running website at `127.0.0.1` and sign in into the admin environment, located
at `127.0.0.1/admin`. 

## Front-end
The front-end is server-side rendered with the Django templating system, however we do use Bootstrap and some JavaScript
magic to properly package this application. In order to update the front-end and compress all images use:

1. Move into the `static` folder.
2. Run `npm start build`, this will do the following:
   - Compile sass into css
   - Compress css
   - Compress JavaScript
   - Compress images
   - Copy high quality images
   - Move all items into the `dist` folder in static.

_Note:_ If you want to keep a high quality copy of an image, then prepend its name with `high`. This image will not be
compressed. 

## Back-end
All the relevant information about the back-end can be found on the corresponding 
[github.io](https://roboteamtwente.github.io/future_factory_website) website