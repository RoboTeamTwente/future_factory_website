# Facts
A fact is a HTML component that contains a big icon and two short pieces of text. They both appear on the main page and 
each team page. 

## Models
There are two models that work with facts, the first one named `Fact` represents a single one.

| Attribute | Description                                                                                                                                                                           |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `icon`    | An icon is one of the many [Themify Icons](https://themify.me/themify-icons). Icons can be picked from a dropdown menu. Hence all the available choices are generated within the code |
| `value`   | This is the big number indicating this fact (maximum of 10 characters)                                                                                                                |
| `context` | Some text that is able to give some context to this number (maximum of 50 characters)                                                                                                 |

Another model that uses facts is a `TeamFact` which inherits the previously described `Fact` model, adding a team to it.
This model is located in the [teams](teams.md) app.