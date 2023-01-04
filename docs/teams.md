# Teams
A team in the context of the Future Factory website is one of the five teams that is located in the Future Factory 
building. Teams have their own webpage where they have some basic information displayed and also a more elaborate
description of their activities.

## Database model
Every team is saved in the database, hence there is a model available for it. Let's go over it:

| Attribute                 | Description                                                                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                    | The name of this team                                                                                                                                |
| `contact_person`          | The name of the main contact person for this team. Usually the communication or team manager                                                         |
| `contact_person_function` | The function of the contact person                                                                                                                   |
| `contact_person_phone`    | The phone number of the contact person, make sure to actually fill out a valid number since people will be able to directily call this from the site |
| `contact_mail`            | The mail-address to use when someone wants to contact the team. Often it looks like info@...                                                         |
| `website`                 | The teams website address                                                                                                                            |
| `banner_picture`          | Each page on the website has a picture shown just below the navigation bar. This is the banner picture that will be shown at this team page          |
| `logo`                    | The team's logo. Preferably a high quality PNG image with a transparent background                                                                   |
| `slogan`                  | The slogan from the team                                                                                                                             |
| `team_picture`            | This will be the first picture that is shown on the website, for consistency reasons this should be the team picture                                 |
| `slug`                    | An auto generated field based on the team name. This field is used to generate the URL to the page of this team                                      |

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

## Creating a new team
When you create a new team in the database, everything should be set up automatically, and you should be good to go. 
However, in order to slightly optimize loading times, the navigation bar is hard-coded. Hence, you will have to the new
team to the navigation bar by hand. The easiest way to do this is by going to the new team in the admin environment, 
click on "view on site" and copying the URL from this page. It can then be placed into the navigation section located
in `templates/basis.html`. The link should look like this:

```html
<li><a href="/teams/team-name/">Team Name</a></li>
```