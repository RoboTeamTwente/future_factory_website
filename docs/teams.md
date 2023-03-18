# Teams
A team in the context of the Future Factory website is one of the five teams that is located in the Future Factory 
building. Teams have their own webpage where they have some basic information displayed and also a more elaborate
description of their activities.

## Database model
Every team is saved in the database, hence there is a model available for it. Let's go over it:

| Attribute                 | Description                                                                                                                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                    | The name of this team                                                                                                                                                                                                  |
| `contact_person`          | The name of the main contact person for this team. Usually the communication or team manager                                                                                                                           |
| `contact_person_function` | The function of the contact person                                                                                                                                                                                     |
| `contact_person_phone`    | The phone number of the contact person, make sure to actually fill out a valid number since people will be able to directily call this from the site                                                                   |
| `contact_mail`            | The mail-address to use when someone wants to contact the team. Often it looks like info@...                                                                                                                           |
| `website`                 | The teams website address                                                                                                                                                                                              |
| `front_page_picture`      | The picture that is being shown on the front page inside of the hexagon. This picture should be square.                                                                                                                |
| `banner_picture`          | Each page on the website has a picture shown just below the navigation bar. This is the banner picture that will be shown at this team page, it will also show up as the picture behind the facts section of this team |
| `logo`                    | The team's logo. Preferably a high quality PNG image with a transparent background                                                                                                                                     |
| `logo_svg`                | The logo in SVG form of this team. This is used on the press page.                                                                                                                                                     |
| `main_color`              | The accent color being used for headers on the team page, the hexagon overlays and icons on the contact form.                                                                                                          |
| `slogan`                  | The slogan from the team                                                                                                                                                                                               |
| `slug`                    | An auto generated field based on the team name. This field is used to generate the URL to the page of this team                                                                                                        |

### Text Sections
As described above, each team has its own page. These pages contain sections where text and images can be uploaded. In 
order to enforce some structure in these sections they are separate models connected to a particular team. Each section
has a title, body and possibly a picture.

| Attribute | Description                                                                                                   |
|-----------|---------------------------------------------------------------------------------------------------------------|
| `title`   | The title of this section                                                                                     |
| `text`    | The body of this section, this is a so-called `QuillField`, which allows for a rich-text editor               |
| `image`   | If wanted, someone can upload an image, which will be presented at the bottom of this text section            |
| `team`    | The team that wants to have this section on their webpage. The admin interface will handle this automatically |

These text sections have a pre-determined ordering. Each page is rendered with sections ordered based on their order of
creation. This should suffice, since the admin interface will correspond with final page render.

### TeamFact
Teams have small facts on their own pages. Each teams is enforced to have 3 or 4 of them on their page. Each fact comes 
with an icon. These icons are [Themify Icons](https://themify.me/themify-icons) and can be chosen with a dropdown menu. 
The database object itself looks like this:

| Attribute | Description                                                   |
|-----------|---------------------------------------------------------------|
| `icon`    | A string representing a Themify Icon                          |
| `value`   | The big font sized text                                       |
| `context` | A smaller piece of text adding context to the number and icon |
| `team`    | To which team does this fact belong?                          |

This object is inherited from the [Fact](facts.md) object.

### TeamAccount
In order to limit teams from editing each other's data each user account has to be connected to a team. Only then that
specific user account can access the team's details in the [administration](https://futurefactorytwente.nl/admin) 
environment.

This model consists out of a one-to-one relation with a Django user and a foreign key with a team object.

## Views
Teams implement two types of views: [`DetailView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#detailview) 
and the [`SendMessage`](contact.md) view. 

The first one displays the team page. It therefore uses the team model and a contact form object for form validation.

The second view handles the submission of a new email. 

## Templates
For the `DetailView` there is a `team.html` template, which shows all the information about a team. The 
`team_thumbnail.html` template generates a single hexagon that can be found on the homepage.

## Creating a new team
When one needs to add a new team, there are quite some steps to be taken. 
1. Create a new user account
2. Create a new team in the database
3. Connect the specific account to the team (`TeamAccount`)
4. Figure out a new nice way to represent the teams on the home screen
   * You will most likely have to update some CSS and perhaps some HTML
5. Furthermore, you'll want to have to update the FF logo throughout the entire website.