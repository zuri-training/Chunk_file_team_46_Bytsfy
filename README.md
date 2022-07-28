#bytsfile_team_46
A webapp that chunks big csv and json files on users specified size

<h1>How does it work?</h1>
<ul style="text-align: center ,">
<li>Login/signup on our website </li>
<li>Upload a file</li>
<li>Specify the chunk size</li>
<li>Specify Number of files</li>
<li>Click on the button</li>
<li>The file will be chunked and saved as .zip, ready for download</li>
</ul>

<h2>Or you want to run locally:</h2>

Clone the project

```
  git clone https://github.com/zuri-training/Chunk_file_team_46_Bytsfy

Go to the project directory
```

cd Chunk_file_team_46_Bytsfy

```
  npm install
```

Create a Virtual Environment
```

python -m venv venv

```

Activate Virtual Environment
```

venv\scripts\activate

```

Install Dependencies
```

pip install -r requirements.txt

```

make migrations
```

python manage.py makemigrations

```

Migrate the database
```

python manage.py migrate

```

create superuser
```

python manage.py createsuperuser

```



Finally, Start The Server.
```

python manage.py runserver

```

<h2>Built with:</h2>
<div class="container" style="width:50%; align-items: center;">
<svg viewBox="0 0 128 128">
<path d="M59.448 0h20.93v96.88c-10.737 2.04-18.62 2.855-27.181 2.855-25.551-.001-38.87-11.551-38.87-33.705 0-21.338 14.135-35.2 36.015-35.2 3.398 0 5.98.272 9.106 1.087zm0 48.765c-2.446-.815-4.485-1.086-7.067-1.086-10.6 0-16.717 6.523-16.717 17.939 0 11.145 5.845 17.26 16.582 17.26 2.309 0 4.212-.136 7.202-.542z"></path><path d="M113.672 32.321V80.84c0 16.717-1.224 24.735-4.893 31.666-3.398 6.661-7.883 10.873-17.124 15.494l-19.435-9.241c9.242-4.35 13.726-8.153 16.58-14 2.99-5.979 3.943-12.91 3.943-31.122V32.321zM92.742.111h20.93v21.474h-20.93z"></path>
</svg>
          
</div>

