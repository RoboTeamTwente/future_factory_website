# News Articles
A news article is usually some form of article describing a past activity that is related with the Future Factory.

## Models
A single model is used by news articles, the `NewsArticle` model.

| Attribute     | Description                                                                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`       | The title of this news article                                                                                                                                   |
| `summary`     | A short piece of text that is only shown on the home page and on the news article list page                                                                      |
| `description` | The main text of this article. Also this field is a `QuillField`, allowing for the end user to add rich-text.                                                    |
| `image`       | The image is used as a cover image and shown next to the article                                                                                                 |
| `visible`     | When you temporarily want to hide this article, but not permanently remove it, you can set this to `False`. Note: Direct links to this article will keep working |
| `date`        | The start date of this event                                                                                                                                     |

## Views
Just like [events](events.md), news articles implement a Detail and a ListView. 

## Templates
The detail view relies on the `news_article.html` template, whereas the list view utilizes the `news.html` template. 
Since news articles are used on multiple places a `news_article_thumbnail.html` is able to generate a single news 
article. This component is used in both the main page and the list view.