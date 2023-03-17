# import PySimpleGUI as sg

# lq = ["a", "b"]
# state = ""
# # ftype = "bold"  # to differentiate b/w query and response
# # fsize = 15  # to differentiate b/w query and response
# # STEP 1 define the layout
# col_1 = [
#     [sg.LB(lq, font=(ftype, fsize), size=(40, 10), key="-LB-")],  # user's query
#     # state of the takeCommand function (reassignment)
#     [sg.Text(state, font=(None, 15), key="-ST-")],
# ]
# col_2 = [
#     [sg.Button('Start', size=(8, 1))],
#     [sg.Button('Terminate', size=(8, 1))],
#     [sg.Button('Mute', size=(8, 1), button_color="red")]
# ]

# layout = [
#     [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2)]
# ]


# # STEP 2 - create the window
# window = sg.Window('My new window', layout)

# # STEP3 - the event loop
# while True:
#     # Read the event that happened and the values dictionary
#     event, values = window.read()
#     print(event, values)
#     # If user closed window with X or if user clicked "Exit" button then exit
#     if event == sg.WIN_CLOSED or event == 'Terminate':
#         break
#     if event == 'Start':
#         state = "aaaa"

#     if event == 'Mute':
#         lq.append()
#         window["-LB-"].update(lq)

# window.close()

import AppOpener as openapp
a = openapp.open("chilgoze")
print(type(a))


# To integrate Spotify in Python, you can use the official Spotify API. Here are the steps to get started:

# 1. First, you need to create a Spotify developer account and register a new application. This will give you credentials to access the Spotify API.

# 2. Next, you can install the `spotipy` library which
# is a Python wrapper for the Spotify Web API. You can
# install it using pip by running `pip install spotipy`.

# 3. Once you have `spotipy` installed, you need to create a Spotify client object and authenticate using your Spotify API credentials. You can do this by running the following code after replacing the CLIENT_ID and CLIENT_SECRET with your own:

#    ```python
#    import spotipy
#    from spotipy.oauth2 import SpotifyClientCredentials

#    client_id = 'YOUR_CLIENT_ID'
#    client_secret = 'YOUR_CLIENT_SECRET'

#    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)   sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#    ```

# 4. Once you have authenticated, you can start using the Spotify Web API. For example, you can search for a track and get its information by running:

#    ```python
#    track_name = 'Smooth'
#    artist_name = 'Santana'

#    result = sp.search(q='artist:' + artist_name + ' track:' + track_name, type='track')
#    track_info = result['tracks']['items'][0]
#    print(track_info)
#    ```

#    This will search for a track named "Smooth" by the artist "Santana" and return its information.

# 5. You can also use the Spotify API to interact with
# user data, such as getting a user's playlists, creating new playlists, and adding songs to playlists.

#    For example, to get a user's playlists, you can run:

#    ```python
#    user_id = 'ENTER_USER_ID'
#    playlists = sp.user_playlists(user_id)
#    for playlist in playlists['items']:
#        print(playlist['name'])
#    ```

#    This will print out the names of all the playlists for the user with the ID specified.

# That's a brief overview of how to integrate Spotify in Python using the Spotify Web API and the `spotipy` library. There are many other features
# you can use with the API, such as searching for artists, albums, and playlists, getting a user's top artists and tracks, and more.
