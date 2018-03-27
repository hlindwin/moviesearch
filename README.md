Hey, sup, hola, shalom,

this app sits here:
https://stormy-lowlands-80953.herokuapp.com/

My slides, from the presentation at Columbus Ohio Python Users Group 
    on March 26, 2018 are here:
https://docs.google.com/presentation/d/18oSHwDSNXn7o_N4aLPtCD1x9ai28DxXNh9J6pC7fELI/edit?usp=sharing

....

What technolgies or code did I use to make this?
    python - the programming language
    
    flask - the website builder
        jinja - the html template engine that flask uses
        
    whoosh - the text indexer aka search engine
    
    scrapy - a web scraping and spider tool
        portia - the graphic user interface of scrapy
        
    heroku - where I deployed the app 
    
        Heroku hosts this code and turns it into a website
    git - I used this to push code to heroku and github
        I also use git to download and upload code to various cloud9 environments
        as well as my computer
        
    github - a place to store code and do version control?
        does git or github do version control? they both do?
        
    virtualenv
        a tool to create virtual environments
        
    pip 
        a tool to install packages
    
    google
        there is where I search my errors
    
    stackoverflow and forums (like c9's)
        this is where I get my answers to my errors and questions
        
    panic
        this is what I did when I didn't have this working and it was 12am
        the day of my presentation. (joke - to show presenters aren't perfect.)
        I was thinking, "Should I email the meetup organizer and cancel?"
        Then, I thought, "No - I'll figure this out in the morning. The important
        thing is my talk vs if my app works."
        Then I went to bed. 
    
    laugh and remember will this matter in 6 months?
        helps me relax and enjoy myself. 
            Like, I accidentally deleted some of my
            code (files and folders) the day of the presentation. I had to 
            google 'how to undelete c9'  There is a way to do it. I had to use 
            the way to recover files to get back the ones w code
            https://community.c9.io/t/how-can-i-recover-the-deleted-folder-directory-from-the-trash/6422
            
        I believe it's more important to get things done 
            even if they aren't perfect.

How I learned to do those technolgies:
    python
        Python for Everybody https://www.py4e.com/
            the book is free on that website
            I believe you can still audit the Coursera course for free
        Automate the Boring Stuff    
            https://automatetheboringstuff.com/
            I had read the chapter on Regular Expressions and the one on CSVs
            I probably should have read the one on web scraping before I did my talk
        Nick Gerakines
            Nick is a friend of my I met at swing dance in Dayton, Ohio.
            I learned from pair programming with him. Especially using os,
            connecting whoosh with outputs from scrapy, and classes + fuctions.
            - you can do pair programming w friends as well!
        
    Command line
        https://learnpythonthehardway.org/book/appendixa.html
        The first 7 are all I really use
        - I didn't get much out of his python course. He does more printing 
            than you need to know off the bat. The second book, first chapters
            are kind of motivational.
        
    flask
        'Learning Flask' tutorial on Lynda
            https://www.lynda.com/Flask-tutorials/Learning-Flask/521231-2.html
            by Lalith Polepeddi from Lynda, "...a Packt author, has been working with Flask 
            since discovering how easy it made learning about web development.
            He's written about Flask for Tuts+, Tech.Pro, and Packt Publishing. 
            Aside from Flask, Lalith is interested in applying computer science 
            to address problems in parallel domains, such as biology."
        
    whoosh
        Nick Gerakines first told me about it.
        Then I read the docs: http://whoosh.readthedocs.io/en/latest/intro.html
        - that documentation is really well written!
    
    scrapy
        their docs: https://doc.scrapy.org/en/latest/intro/tutorial.html
        an improvement for this to add selenium
            this seems to answer some of my windowing or frame problems
            Python Automation - 1. Scraping the Web with Selenium and Python 
                by Chris Hawkes https://www.youtube.com/watch?v=yhFjXskURFU
    
    cloud9
        I first learned about cloud9 from https://upskillcourses.com/
        I used cloud9 aka c9 to develop in.
        Amazon bought c9 and it is now part of AWS. You have to get an AWS account to
        use it. That process is kind of terrible.
        
        Once you get into c9, the way I was able to get to be able to use heroku 
        command line interface was these commands:
            
            $ nvm install v9.9.0  
            $ npm install -g cli-engine-command@8.0.0 
            $ npm install -g heroku-cli 

    git
        this wasn't easy to learn. I did a bunch of googling.
        My friends Greg Rearden https://www.linkedin.com/in/gregoryrearden
        and Daniel Lecklider https://www.linkedin.com/in/daniel-lecklider
        helped me figure it out initially.
        I also learned from upskillcourses's videos.
       
        Essentially you need these commands
            setup
                git init
                git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
                
            once things are setup
                git add .  # that adds stuff 
                git status # see what you added
                git commit -m 'a comment is required'
                git push origin master #you have now updated the thing
                
            if you made changes somewhere else
                git pull origin master
                
                    or if from heroku
                    
                git pull heroku master --rebase
            
        there are a few demos now. 
        I have definitely erased projects before!
        practice on some dummy repos and back up your stuff as you learn
        https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
        
        I didn't like https://try.github.io/levels/1/challenges/1
        

    virtualenv
        their documentation is good. https://virtualenv.pypa.io/en/stable/
        I was never really sure where to put the virtualenv. I think the best 
            answer is outside your project folder. Then cd aka change directory
            into your project folder.
            
If you downloaded this code and want to get it to work, you will need to:
1) Download and install python3 - go for the newest version
2) create a virtualenv (recommended)
    a) to learn how to use this https://virtualenv.pypa.io/en/stable/userguide/
3) $ pip install -r /path/to/requirements.txt



Notes for Harry
Create a requirements.txt file:
    $ pip freeze>requirements.txt

git 
    One of them created a folder named: ”/
    I think that happened when it was trying to install or update nvm. bc
    '”/home/ec2-user/.nvm”/versions/node/v9.9.0/share/systemtap/tapset/node.stp'
   
   listing files in a github
   
        git ls-files file_name
        
    removing files
            
        For single file:
        
            git rm --cached mylogfile.log
        
        For single directory:
        
            git rm --cached -r mydirectory                          

    pushing to github
        git remote add origin https://github.com/hlindwin/moviesearch.git
            git push -u origin master

         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!


https://stackoverflow.com/questions/2047465/how-can-i-delete-a-file-from-git-repo
git rm --cached file1.txt
git commit -m "remove file1.txt"
https://stackoverflow.com/questions/6313126/how-to-remove-a-directory-from-git-repository
git rm -r --cached myFolder



https://devcenter.heroku.com/articles/collaborating