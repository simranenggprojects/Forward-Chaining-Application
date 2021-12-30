# importing libraries
from durable.lang import *

# simple print messages as welcome note
def printmsg():
    print("\n\n--------------------------------")
    print("Welcome to Avvisare Fratello")
    print("--------------------------------")
    userName = input("What's your name? ")
    print("\nHi {0}, Hope you are having a great time at IIITD.".format(userName))
    print("I am Avvisare Fratello and would love to help you with Course Suggestion")
    print("\nI really hope that I can help you well, but")
    print("help me to help you, please answer some questions.")
    print("\n----------------------------------------------")
    print("Here are few questions for Course Suggestion")
    print("----------------------------------------------")
    print("\nWhich specialization are you going in for?")
    print('-> Artificial Intelligence')
    print('-> Data Engineering')
    print('-> Information Security')
    spl = input("Enter here: ")
    print("\nWell... very good so far! Please tell me what sort of courses are you looking for?")
    print("-> Theory (Write t)")
    print("-> Non Theory (Write n)")
    print("Here, no course is pure theory/ pure non theory, these terms refer to where it tends more.")
    spltype = input("Enter here: ")
    print("\nOne last information! Won't bother you anymore! What level of course you really want?")
    print("-> Advanced (Write a)")
    print("-> Intermediate (Write i)")
    lvl = input("Enter here: ")
    return spl, spltype, lvl

# encoding specializations for ease of referance further
def encode(spl):
    if spl == 'Artificial Intelligence':
        spl = 'ai'
    elif spl == 'Data Engineering':
        spl = 'de'
    elif spl == 'Information Security':
        spl = 'is'
    return spl

# subject and code
# providing full form to abbreviations
# also mentioning code through which website link will be generated
def encode_sub(str):
    if str == 'ml':
        sub,c = 'MACHINE LEARNING', 'CSE343'
    elif str == 'ai':
        sub,c = 'ARTIFICIAL INTELLIGENCE', 'CSE643'
    elif str == 'ga':
        sub,c = 'GRADUATE ALGORITHMS', 'CSE525'
    elif str == 'dmg':
        sub,c = 'DATA MINING', 'CSE506'
    elif str == 'nlp':
        sub,c = 'NATURAL LANGUAGE PROCESSING', 'CSE556'
    elif str == 'dl':
        sub,c = 'DEEP LEARNING', 'CSE641'
    elif str == 'dbsi':
        sub,c = 'DATABASE SYSTEM IMPLEMENTATION', 'CSE507'
    elif str == 'dw':
        sub,c = 'DATA WAREHOUSING', 'CSE606'
    elif str == 'tmc':
        sub,c = 'THEORY OF MODERN CRYPTOGRAPHY', 'CSE524'
    elif str == 'nsc':
        sub,c = 'NETWORK SECURITY', 'CSE350'
    elif str == 'ac':
        sub,c = 'APPLIED CRYPTOGRAPHY', 'CSE546'
    elif str == 'se':
        sub,c = 'SECURITY ENGINEERING', 'CSE552'
    return sub,c

# based on inputs by user
with ruleset('takecourse'):
    # must take course for ai
    @when_all((m.area == 'ai'))
    def func(c):
        c.assert_fact({'subject':'ml'})
        c.assert_fact({'subject': 'ai'})

    # must take course for de
    @when_all((m.area == 'de'))
    def func(c):
        c.assert_fact({'subject': 'dmg'})
        c.assert_fact({'subject': 'dw'})

    # must take course for is
    @when_all((m.area == 'is'))
    def func(c):
        c.assert_fact({'subject': 'nsc'})
        c.assert_fact({'subject': 'ga'})

    # rest are based on user's interest

    @when_all((m.area == 'ai') & (m.spltype == 't') & (m.lvl == 'i'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'ml'})
        c.assert_fact('subjects', {'ele': 'ai'})
        c.assert_fact('subjects', {'ele': 'ga'})

    @when_all((m.area == 'ai') & (m.spltype == 'n') & (m.lvl == 'i'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'dmg'})

    @when_all((m.area == 'ai') & (m.spltype == 't') & (m.lvl == 'a'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'nlp'})

    @when_all((m.area == 'ai') & (m.spltype == 'n') & (m.lvl == 'a'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'dl'})

    @when_all((m.area == 'de') & (m.spltype == 't') & (m.lvl == 'i'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'ml'})
        c.assert_fact('subjects', {'ele': 'ga'})

    @when_all((m.area == 'de') & (m.spltype == 'n') & (m.lvl == 'i'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'dmg'})
        c.assert_fact('subjects', {'ele': 'dw'})

    @when_all((m.area == 'de') & (m.spltype == 'n') & (m.lvl == 'a'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'dbsi'})

    @when_all((m.area == 'de') & (m.spltype == 't') & (m.lvl == 'a'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'nlp'})

    @when_all((m.area == 'is') & (m.spltype == 't') & (m.lvl == 'a'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'tmc'})

    @when_all((m.area == 'is') & (m.spltype == 't') & (m.lvl == 'i'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'nsc'})

    @when_all((m.area == 'is') & (m.spltype == 'n') & (m.lvl == 'a'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'ac'})

    @when_all((m.area == 'is') & (m.spltype == 'n') & (m.lvl == 'i'))
    def func(c):
        c.assert_fact('subjects', {'ele': 'se'})

    # output for must take courses
    @when_all(+m.subject)
    def output(c):
        sub,code = encode_sub(c.m.subject)
        print()
        print("-> YOU HAVE TO TAKE THIS COURSE IRRESPECTIVE OF YOUR CHOICE")
        print('-> MUST TAKE COURSE: {0}'.format(sub))
        print('   COURSE DETAILS: http://techtree.iiitd.edu.in/viewDescription/filename?={0}'.format(code))

# asserting facts for subjects
with ruleset('subjects'):
    @when_all(m.ele == 'ml')
    def do1(d):
        d.assert_fact({'subject': 'ml'})

    @when_all(m.ele == 'ai')
    def do2(d):
        d.assert_fact({'subject': 'ai'})

    @when_all(m.ele == 'ga')
    def do3(d):
        d.assert_fact({'subject': 'ga'})

    @when_all(m.ele == 'dmg')
    def do4(d):
        d.assert_fact({'subject': 'dmg'})

    @when_all(m.ele == 'nlp')
    def do5(d):
        d.assert_fact({'subject': 'nlp'})

    @when_all(m.ele == 'dl')
    def do6(d):
        d.assert_fact({'subject': 'dl'})

    @when_all(m.ele == 'dbsi')
    def do7(d):
        d.assert_fact({'subject': 'dbsi'})

    @when_all(m.ele == 'dw')
    def do8(d):
        d.assert_fact({'subject': 'dw'})

    @when_all(m.ele == 'tmc')
    def do9(d):
        d.assert_fact({'subject': 'tmc'})

    @when_all(m.ele == 'nsc')
    def do10(d):
        d.assert_fact({'subject': 'nsc'})

    @when_all(m.ele == 'ac')
    def do11(d):
        d.assert_fact({'subject': 'ac'})

    @when_all(m.ele == 'se')
    def do12(d):
        d.assert_fact({'subject': 'se'})

    # output for courses that are as per user's interest
    @when_all(+m.subject)
    def output(d):
        sub, code = encode_sub(d.m.subject)
        print()
        print('-> CAN TAKE COURSE (AS PER YOUR INTEREST): {0}'.format(sub))
        print('   COURSE DETAILS: http://techtree.iiitd.edu.in/viewDescription/filename?={0}'.format(code))

# printing note for extra curricular activities
def printmsg2():
    print("\nAdmist of courses tension, don't skip extra curricular activities.")
    print("Believe me, they won't waste your time, but increase your productivity.")
    print("At IIITD, there are a lot of clubs, you are interested in ")
    print("-> Technical")
    print("-> NonTechnical")
    ch = input("Enter here: ")
    return ch

# printing note for technical clubs
def tech():
    print("\nSo, within technical what are you interested into?")
    print("-> Coding")
    print("-> DataScience")
    print("-> Security")
    print("-> ProductDesign")
    print("-> Hardware")
    print("-> Maths")
    print("-> TechCommunity")
    cht = input("Enter here: ")
    return cht

# printing note for non technical clubs
def nontech():
    print("\nSo, within non-technical what are you interested into?")
    print("-> Literature, Philosophy, Art (Write a)")
    print("-> NGO (Write b)")
    print("-> Music, Theatre, Dance (Write c)")
    print("-> Humour (Write d)")
    print("-> Fashion (Write e)")
    print("-> Food and Fun (Write f)")
    print("-> Photography (Write g)")
    print("-> Chess (Write h)")
    cht = input("Enter here: ")
    return cht

# rules for co-curricular activities as per interest of user
with ruleset('curricular'):
    @when_all((m.domain == 'Technical') & (m.domtype == 'Coding'))
    def club(e):
        e.assert_fact({'subject': 'ACM Student Chapter, Byld, Cyborg, Foobar, IEEE'})

    @when_all((m.domain == 'Technical') & (m.domtype == 'DataScience'))
    def club(e):
        e.assert_fact({'subject': 'Lean, BioBytes'})

    @when_all((m.domain == 'Technical') & (m.domtype == 'Security'))
    def club(e):
        e.assert_fact({'subject': 'DarkCode'})

    @when_all((m.domain == 'Technical') & (m.domtype == 'ProductDesign'))
    def club(e):
        e.assert_fact({'subject': 'DesignHub'})

    @when_all((m.domain == 'Technical') & (m.domtype == 'Hardware'))
    def club(e):
        e.assert_fact({'subject': 'Electroholics, Cyborg'})

    @when_all((m.domain == 'Technical') & (m.domtype == 'Maths'))
    def club(e):
        e.assert_fact({'subject': 'Evariste'})

    @when_all((m.domain == 'Technical') & (m.domtype == 'TechCommunity'))
    def club(e):
        e.assert_fact({'subject': 'Lean, Women in Tech'})

    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'a'))
    def club(e):
        e.assert_fact({'subject': 'LitSoc, PhiloSoc, Meraki'})


    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'b'))
    def club(e):
        e.assert_fact({'subject': 'GirlUp, Enactus'})


    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'c'))
    def club(e):
        e.assert_fact({'subject': 'Audiobytes, Machaan, Madtoes'})


    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'd'))
    def club(e):
        e.assert_fact({'subject': 'MicDrop'})

    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'e'))
    def club(e):
        e.assert_fact({'subject': 'Muse'})

    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'f'))
    def club(e):
        e.assert_fact({'subject': 'Salt N Pepper'})

    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'g'))
    def club(e):
        e.assert_fact({'subject': 'Tasveer'})

    @when_all((m.domain == 'NonTechnical') & (m.domtype == 'h'))
    def club(e):
        e.assert_fact({'subject': 'The 65th Square'})

    @when_all(+m.subject)
    def output(e):
        print()
        print("\n-------------------------------HERE ARE YOUR RESULTS-------------------------------\n")
        print('You can join following club(s): {0}'.format(e.m.subject))

# the main function
if __name__ == '__main__':
    spla, spltypea, lvla = printmsg()
    spla = encode(spla)
    print("\n-------------------------------HERE ARE YOUR RESULTS-------------------------------")
    assert_fact('takecourse',{'area':spla, 'spltype':spltypea, 'lvl':lvla})
    print("\n-----------------------------------------------------------------------------------")
    ch = printmsg2()
    print("\n-----------------------------------------------------------------------------------")
    if ch == 'Technical':
        cht = tech()
    elif ch == 'NonTechnical':
        cht = nontech()
    assert_fact('curricular',{'domain':ch,'domtype':cht})
    print("For more details, visit: http://studentcouncil.iiitd.edu.in/clubs.html")
    print("Also, great news is that you can open your own club")
    print("\n-----------------------------------------------------------------------------------")
    print("\n\tI HOPE THAT I WAS ABLE TO HELP YOU A BIT. HAVE A GREAT DAY!")
    print("\n-----------------------------------------------------------------------------------")


