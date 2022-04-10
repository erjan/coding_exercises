'''

Pub/Sub pattern is a wide used pattern in system design. In this problem, you need to implement a pub/sub pattern to support user subscribes on a specific channel and get notification messages from subscribed channels.

There are 3 methods you need to implement:

subscribe(channel, user_id): Subscribe the given user to the given channel.
unsubscribe(channel, user_id): Unsubscribe the given user from the given channel.
publish(channel, message): You need to publish the message to the channel so that everyone subscribed on the channel will receive this message.
Call PushNotification.notify(user_id, message) to push the message to the user.

'''



'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''
class PubSubPattern:
    subs = {}
    def __init__(self):
	    pass
    # do intialization if necessary 

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """
    def subscribe(self, channel, user_id):
        # write your code here
        if channel not in self.subs:
            self.subs[channel] = set()
        self.subs[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
    	# write your code here
        if channel in self.subs and user_id in self.subs[channel] :
        	self.subs[channel].remove(user_id)
    	
    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """

    def publish(self, channel, message):
		# write your code here
        if channel in self.subs and len(self.subs[channel]) != 0:
            for id in self.subs[channel] :
                PushNotification.notify(id, message)
