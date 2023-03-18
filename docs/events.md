# Events
An event is some form of activity that starts on a given time and date.

## Models
There is a single [model](https://docs.djangoproject.com/en/4.1/topics/db/models/) available in this app, which
represents a model.

| Attribute     | Description                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`       | The title of this event                                                                                                                                        |
| `summary`     | A short piece of text that is only shown on the home page and on the events list page                                                                          |
| `description` | The main text description this event. Also this field is a `QuillField`, which provides the user a rich-text editor                                            |
| `image`       | The image is used as a cover image and shown with this event.                                                                                                  |
| `visible`     | When you temporarily want to hide this event, but not permanently remove it, you can set this to `False`. Note: Direct links to this article will keep working |
| `date`        | The start date and time of this event                                                                                                                          |
| `location`    | Where this event is supposed to take place                                                                                                                     |

## Views
For events, both the [`DetailView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#detailview)
and the [`ListView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview) have been
implemented. The list view sorts the events based on their start date / time. A 
[paginator](https://docs.djangoproject.com/en/4.1/topics/pagination/) makes sure that every page has a maximum of eight 
events on display at the same time.

## Templates
Next to your basic detail and list view templates an event also has a `event_thumbnail.html` template. This template
generates a single event item. This template is both used in the ListView as on the main page.