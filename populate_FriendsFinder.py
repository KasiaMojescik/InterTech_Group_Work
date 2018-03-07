import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
						'group_project.settings')
import django

django.setup()

from django.contrib.auth.models import User
from FriendsFinder.models import Character, Thread, ThreadComment
from random import randint

#Create Users, Characters that link to users, Threads created by characters, comments created by characters

def populate():
    userLim = 10
    threadLim = 25
    commentLim = 100

    users = create_users(limit=userLim)
    characters = create_characters(users, limit=threadLim)
    #threads = create_threads(characters, threadLim)
    #create_comments(threads,characters, commentLim)

#Create user accounts (required before Character creation)
def create_users(limit=25):
    testusers = []

    for count in range(0,limit):
        current = User.objects.create(username="testuser_" + str(count))
        current.save()
        testusers.append(current)
    return testusers

#Create characters and bypass quiz by randomly giving a friends character name
def create_characters(users, limit):
    characterNames  = ['Joey','Chandler','Ross','Rachel','Phoebe','Monica']
    testCharacters = []

    for user in users:
        #current = Character.objects.create(characterName=characterNames[randint(0,characterNames.count())],linkedUser=user)
        print characterNames[randint(0,characterNames.count())]
        #current.save()
        #testCharacters.append(current)
    return testCharacters

#Create threads by picking a user as random limit times
def create_threads(characters, limit):
    threads = []

    for count in range(0,limit):
        current = Thread.objects.create(threadCreator=characters[randint(0, characters.count())], threadTitle="test" + str(count), threadContent="test" + str(count))
        current.save()
        threads.append(current)
    return threads

#Create comments by randomly selecting a thread and character
def create_comments(threads, characters, limit):

    for count in range(0,limit):
        currentCharacter = characters[randint(0, characters.count())]
        currentThread = threads[randint(0,threads.count())]

        current = ThreadComment.objects.create(threadCommentParent = currentThread, threadCommentCreator=currentCharacter, threadCommentContent="COMMENT BY " + currentCharacter.characterName)
        current.save()
    return

# Start execution here!
if __name__ == '__main__':
	print("Starting FriendsFinder population script...")
	populate()