class Comment:
    def __init__(self, value, author):
        self.value = value
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        if isinstance(reply, Comment):
            self.replies.append(reply)
        else:
            raise TypeError("Reply must be an instance of Comment.")

    def remove_reply(self):
        self.value = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = '\t' * level
        print(f'{indent}{self.author}: {self.value}')
        for reply in self.replies:
            reply.display(level+1)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
