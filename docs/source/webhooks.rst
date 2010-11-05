.. _webhooks_toplevel:

==================
Webhooks
==================

publish
=======

Send a message to all users subscribed to a channel.

Webhook Form Variables:

* ``channel_name``: The name of the channel the message is being published to.
* ``payload``: The json payload to send to all users subscribed to the channel.

Webhook post includes sender cookies.

Returns json:

.. sourcecode:: javascript

    [ success (boolean) , details (object) ]


Optional Webhook return details:

* ``override_payload``: A new payload that will be published instead of the original payload.
* ``only_to_sender``: If true, the message will only be published to the sender instead of all the users subscribed the channel.
* ``error``: If success is false, error text to return to sender.


Example:

Client Calls:

.. sourcecode:: javascript

    connection.publish("channel-1", { title: "a message", body: "some text" });


Webhook Called With:

.. sourcecode:: javascript

    { channel_name: "channel-1", payload: { title: "a message", body: "some text" } }


Webhook replies:

.. sourcecode:: javascript

    [ true, { } ]


And the following frame is published all subscribers to the channel 'channel-1':

.. sourcecode:: javascript

    { channel_name: "channel-1", "payload": { title: "a message", body: "some text" } }


message
=======

Send a private message to a user.

Webhook Form Variables:

* ``sender``: The user name of the sending user.
* ``recipient``: The user name of the receiving user.
* ``recipient_exists``: True if the recipient name is that of a connected user, false otherwise.
* ``payload``: The json payload to send to the receiving user.

Webhook post includes sender cookies.

Returns json:

.. sourcecode:: javascript

    [ success (boolean) , details (object) ]


Optional Webhook return details:

* ``override_payload``: A new payload that will be sent instead of the original payload.
* ``override_recipient_name``: The name of a user to send the message to instead of the original reciepient.


Example:

Client Calls:

.. sourcecode:: javascript

    connection.message("mcarter", { title: "a message", body: "some text" });


Webhook Called With:

.. sourcecode:: javascript

    { sender: "some_user", recipient: "mcarter", payload: { title: "a message", body: "some text" } }


Webhook replies:

.. sourcecode:: javascript

    [ true, { override_payload: { title: "a new title", body: "some text" } } ]


And the following frame is published to the user 'mcarter':

.. sourcecode:: javascript

    { sender: "some_user", recipient: "mcarter", "payload": { title: "a new title", body: "some text" } }



