# Events
An event is something that happened (or will happen) at the Future Factory. Events are small articles where we share
what happened and what was achieved during such event or activity.

## Database model
Every event is saved in the database, lets take a look at the model that is used.

| Attribute     | Description                                                                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`       | The title of this event or article                                                                                                                               |
| `summary`     | A short piece of text that is only shown on the home page and on the news list page                                                                              |
| `description` | The article itself. Also this field is a `QuillField`, allowing for rich-text.                                                                                   |
| `image`       | The image is used as a cover image and shown next to the article                                                                                                 |
| `visible`     | When you temporarily want to hide this article, but not permenantly remove it, you can set this to `False`. Note: Direct links to this article will keep working |
| `event_date`  | The start date of this event                                                                                                                                     |

Next to default functions this model has a property named `description_html`. This strips of the new paragraphs after 
someone has pressed on enter in the rich-text editor, causing a lot of unnecessary white space.

## Page rendering
When events are displayed in a list, they are first filtered based on their visibility. Then sorted on the event date. 