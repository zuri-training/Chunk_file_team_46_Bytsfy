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
<div class="container" >

<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" alt="django width="60" height="60">
          
</div>

