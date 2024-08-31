# Модель (Model)
class Article:
    def __init__(self, title, author, character_count, publication, description):
        self.title = title
        self.author = author
        self.character_count = character_count
        self.publication = publication
        self.description = description

    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, Characters: {self.character_count}, "
                f"Publication: {self.publication}, Description: {self.description}")


# Контроллер (Controller)

class ArticleController:
    def __init__(self, model):
        self.model = model

    def update_title(self, new_title):
        self.model.title = new_title

    def update_author(self, new_author):
        self.model.author = new_author

    def update_character_count(self, new_character_count):
        self.model.character_count = new_character_count

    def update_publication(self, new_publication):
        self.model.publication = new_publication

    def update_description(self, new_description):
        self.model.description = new_description


# Представление (View)

def display_publication(publication):
    print(f"Publication: {publication}")


class ArticleView:
    def display_article_details(self, article):
        print(article)

    def display_title(self, title):
        print(f"Title: {title}")

    def display_author(self, author):
        print(f"Author: {author}")

    def display_character_count(self, character_count):
        print(f"Character Count: {character_count}")

    def display_description(self, description):
        print(f"Description: {description}")


if __name__ == "__main__":
    # Создание модели
    article = Article("Initial Title", "Initial Author", 1000,
                      "Initial Publication", "Initial Description")

    # Создание контроллера
    controller = ArticleController(article)

    # Создание представления
    view = ArticleView()

    # Отображение первоначальных данных статьи
    view.display_article_details(article)

    # Обновление данных статьи через контроллер
    controller.update_title("New Title")
    controller.update_author("New Author")
    controller.update_character_count(2000)
    controller.update_publication("New Publication")
    controller.update_description("New Description")

    # Отображение обновленных данных статьи
    view.display_article_details(article)
