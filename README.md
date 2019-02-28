<div style="text-align:center">
<h1 style="font-weight: bold">FlightList</h1>
<img src="https://image.flaticon.com/icons/svg/61/61212.svg" width="200"/>
</div>

<h2 style="font-weight: bold">Your New Aviation Journal</h2>

<p>FlightList is a straightforward journaling application meant for users to record their planespotter and avgeek experiences. Users have full create, read, update, and delete functionality over their journal experiences. FlightList is built using Django and Python and takes advantage of Django's built in authentication features to handle registration and log in.</p>

<h2>Instructions for Installing FlightList</h2>

<h4> You will need to have command line tools installed for your computer to use terminal commands.
</h4>

  * Mac users - Open your terminal and type

    ```sh
    git --version
    ```

  * Linux/Windows users, please vist the [Git page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and follow the instructions for setup

<h4>You will now need to configure your git account. In the terminal window, type</h4>

  ```sh
  git config –global user.name “You Name”
  git config –global user.email “Your Email”
  ```

#### Create a new directory to store the files in. Type this into your terminal window.

  ```sh
  mkdir FlightList
  cd FlightList
  git clone https://github.com/zacjones91/flightlist
  ```

#### If you do not have Python version 3 installed on your machine, visit the [Python Download Page](https://www.python.org/downloads/) or to install with command line,

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
pip install django
```
#### Now you need to migrate the models into your local folder:
```sh
python manage.py makemigrations
python manage.py migrate
```

#### You can now run the program by typing:

```sh
python manage.py runserver 8080
```

<h1 style="text-align:center; font-weight: bold;">Congratulations! You are now experiencing FlightList!

<h2 style="font-weight:bold;text-align:center" > Main functionality of FlightList</h2>

1. New users can register. Already registered users can log in to their existing accounts.
2. When user clicks All Entries in the navigation bar, a list will appear showing all of that user's entries.
3. When user clicks on the entry's detail button, the entry's details will appear on a new page, showing the full journal entry and image.
4. When the user clicks New Entry, they will be presented with a form to create and save a new journal entry.
5. When the user clicks Edit Entry, they will be presented with a form to update the selected journal entry. The form will be pre-filled with the previous entry.
6. When the user clicks Delete Entry, they will be presented with a confirmation alert. If the user confirms the delete, the selected entry will be deleted.
```