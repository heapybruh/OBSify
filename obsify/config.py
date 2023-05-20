class Widget():
    def __init__(self, position: str = "leftup"):
        self.position = position

    def to_dict(self):
        return self.__dict__

class Config():
    def __init__(self, client_id: str, client_secret: str, redirect_url: str, widget: Widget):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        self.widget = widget

    def to_dict(self):
        return {"client_id": self.client_id, "client_secret": self.client_secret, "redirect_url": self.redirect_url, "widget": self.widget.to_dict()}