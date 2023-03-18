# Styling
The front-end of this website has been written with the help of [Bootstrap](https://getbootstrap.com/), 
[jQuery](https://jquery.com/) and [Themify Icons](https://themify.me/themify-icons). Furthermore, the website
is based of a template provided by DevCRUD (https://devcrud.com). 

In order to update the generated `.css` and `.js` files [NodeJS](https://nodejs.org/en) in a combination with 
[gulp.js](https://gulpjs.com/) is being used. 

When working on the front-end you can find all the images, stylesheets and other files inside the 
`/static/public_htnl/assets` folder. When you're done with editing, and you want to see the result locally follow the 
following steps:
1. Open a terminal inside of `/static`.
2. If `node_modules` is not yet in this directory, run `npm install`
3. Run `npm start clean`, removing all the old production files.
4. Run `npm start build`, this will start compiling the (s)css, js, compressing images etc. This will take some time,
   if you only want to update for example the css, you can do so by running `npm start css` and then `npm start scss`.

## Deployment
This is a note for the person that is responsible for deploying any updates. When asset files have been updated they 
might not always be detected by the input-free `collectstatic` command from Django. So if you are missing any new assets
re-run the `python manage.py collectstatic` command by hand.