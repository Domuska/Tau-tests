# -*- coding: utf-8 -*-
class NotesTests(UITestCase):
    
    def setUp(self):
        launch.activity('com.nononsenseapps.notepad', '.activities.ActivityList')
        
        #launch.app('com.android.settings'
        #launch.app('com.android.chrome')
        
    def tearDown(self):
        kill('com.nononsenseapps.notepad')
        packages.clearData('com.nononsenseapps.notepad')
        
        

    @testCaseInfo('<Add a new note>', deviceCount=1)
    def testAddNewNoteShouldShowNameInNotesScreen(self):
        """ Insert brief description of the test case

            1. Close the navigation drawer
            2. Tap on the fab
            3. Enter the name for the note and close the note
            4. Verify that the note is in the list
           
        """
        # goto('Notes')
        log('Step1: Insert test step description')
        #tap.description('Apps')
        #tap.description('Notes')
        swipe.description('List of tasks').to.location((0, 0.5))
        tap.description('Floating action button')
        tap.text('Note')
        input.text('prepare food')
        tap.description('Navigate up')
        verify.text('prepare food', scroll=True)
        

    @testCaseInfo('<Add new notelist>', deviceCount=1)
    def testAddTaskListCheckItIsAddedToDrawer(self):
        """
            1. do stuff
        """
        #goto('Notes')
        #tap.description('Apps')
        #tap.description('Notes')
        #tap.description('List of tasks')
        #tap.description('Apps')
        #tap.description('Notes')
        tap.text('Create new')
        input.text('a random tasklist')
        tap.text('OK')
        exists.toast('Saved') # sender = 'com.nononsenseapps.notepad'
        tap.description('Open navigation drawer')
        verify.text('a random tasklist', scroll=True)
        
        
        
