class YouTubeChannel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, video):
        for subscriber in self.subscribers:
            subscriber.update(video)

    def upload_video(self, video):
        print(f"Uploaded: {video}")
        self.notify(video)

class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, video):
        print(f"{self.name} received notification: {video}")

# usage

arjun = Subscriber("Arjun")
rahul = Subscriber("Rahul")
anu = Subscriber("Anu")

channel = YouTubeChannel()

channel.subscribe(arjun)
channel.subscribe(rahul)
channel.subscribe(anu)

channel.upload_video("Observer Pattern Tutorial")


# Output:

# Uploaded: Observer Pattern Tutorial

# Arjun received notification: Observer Pattern Tutorial
# Rahul received notification: Observer Pattern Tutorial
# Anu received notification: Observer Pattern Tutorial