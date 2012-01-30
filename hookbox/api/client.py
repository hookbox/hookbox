#!/usr/bin/env python

from eventlet.green import httplib, urllib

class Client (object):
    """ Hookbox REST api client.
    Creates a persistent, HTTP/1.1 connection to the hookbox server.
    """ 

    def __init__ (self, server_ip, server_port):
        """ Open an HTTP connection to the hookbox server.
        """
        self.conn = httplib.HTTPConnection(server_ip, server_port)
        self.headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}

    def _transmit(self, command, data):
        enc_data = urllib.urlencode(data)
        self.conn.request('POST', '/web/%s'%command, enc_data, self.headers)
        resp = self.conn.getresponse()
        return resp.read()

    def publish (self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name: 
            payload:
        """
        return self._transmit("publish", data)

    def subscribe(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name: 
            name:
        """        
        return self._transmit("subscribe", data)

    def unsubscribe(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name: 
            name:
        """        
        return self._transmit("subscribe", data)

    def get_channel_info(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name: 
        """        
        return self._transmit("get_channel_info", data)

    def set_channel_options(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name:
            
        Optional Variables:
            anonymous: json boolean
            history: json list in the proper history format
            history_size: json integer
            moderated: json boolean
            moderated_publish: json boolean
            moderated_subscribe: json boolean
            moderated_unsubscribe: json boolean
            polling: json object in the proper polling format
            presenceful: json boolean
            reflective: json boolean
            state: json object
        """
        return self._transmit("set_channel_options", data)

    def create_channel(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name: 
        """        
        return self._transmit("create_channel", data)

    def destroy_channel(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name: 
        """        
        return self._transmit("destroy_channel", data)

    def state_set_key(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name:
        
        Optional Values:
            key: The target key in the state
            val: any valid json structure; it will be the new value of the given key on the state
        """        
        return self._transmit("state_set_key", data)

    def state_delete_key(self, data):
        """
        Required keys in data dictionary:
            security_token: 
            channel_name:
        
        Optional Values:
            key: The target key in the state to delete
        """
        return self._transmit("state_delete_key", data)

