from enum import Enum


class TagType(Enum):
    LINK = 0
    IMAGE = 1
    PARAGRAPH = 2


class Tag:
    def __init__(self, tag_name: str):
        self.tag_name = tag_name

    def display(self):
        return f"<{self.tag_name}></{self.tag_name}>"


class Link(Tag):
    def __init__(self):
        super().__init__('a')


class Image(Tag):
    def __init__(self):
        super().__init__('img')


class Paragraph(Tag):
    def __init__(self):
        super().__init__('p')


def create_tag(tag_type: TagType):
    factory_dict = {
        TagType.LINK: Link,
        TagType.IMAGE: Image,
        TagType.PARAGRAPH: Paragraph
    }
    return factory_dict[tag_type]()


def main():
    for tag in TagType:
        my_tag = create_tag(tag)
        print(f'Тип тега: {tag}, вид в HTML: {my_tag.display()}')


if __name__ == '__main__':
    main()




