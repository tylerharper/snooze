Use
===

  The first step in using any RESTful api is knowing the base site that it is
  attached to.

  < INSERT INFO HERE >

  For every slash and command ("/something") in a restful api you will use a
  dot and a function call for that command (".something()").
 
  However you do not have to use that function call. You can override the function
  name to be anything you like.  An example git hub api could look both ways
 
    url: http://github.com/api/v2/json/user/show/knobe
   
    sleepy api: 
    raft.api.v2.json.user.show.knobe
    or
    raft.api.v2.json.user.show.username('knobe')
   
 
  The last call will replace the username call with knobe.  This makes it easier to use
  if you want to inherit the class and use it another way.  If you leave it blank it will
  give you the api url:
 
    http://github.com/apu/v2/json/user/show/username
 
 
 Also you can pass POST or GET request with the options. Using the url from
 the previous example your code should look like this
 
    raft.api.v2.json.user.show.username('knobe', name='New Name')
 
 As you see the api can get ugly fast. Maybe you want to set api.v2.yamel
 to be included in the restful call.  You can do this by adding a prefix
 or adding it to your base url.
 
    raft.add_prefix('api.v2.yamel') # it can be dots
    or
    raft.add_prefix('api/v2/yamel') # or slashes if you forget and end slash or add and extra slash it there we take care of it
 
Acknowledgments
===============
  Mike Verdone and his twitter api, because without his api
  the idea would not have made it out of my mind. 

