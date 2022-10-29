class Start:
    def __init__(self):
        WritePost()


class WritePost:
    def __init__(self):
        self.text = None
        self.push_date = None
        self.write_post()

    def write_post(self):
        self.text = input("Write a text: ")
        try:
            self.push_post(int(input("Do you want to publish the text (1/0): ")))
        except ValueError:
            print("Sadece 0 ya da 1 girilebilir.")
            return self.write_post()

    def push_post(self, order):
        if order:
            self.__push_postdatabase()
        else:
            exit()

    def __push_postdatabase(self):
        if self.text:
            pass
            #self.text and self.push_date
